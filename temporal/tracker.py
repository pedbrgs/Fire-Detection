# Based on Simple Object Tracking with OpenCV by pyimagesearch 
# https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/

import numpy as np
from scipy.stats import variation
from collections import OrderedDict
from scipy.spatial import distance as dist

class Log():

    def __init__(self):

        self.coord_objs = list()
        self.classes = list()
        self.conf_scores = list()
        self.detection_time = list()
        self.areas = OrderedDict()
        self.centroids = OrderedDict()
        self.first_frame = True

    def update(self, centroids, areas):

        # Loop over the tracked objects(id, areas) in log.areas.items():
        for (id, _) in areas.items():

            if id != None:
                # If the log of the object "id" already exists, just add the values
                try:
                    self.areas[id].append(areas[id])
                    self.centroids[id].append(centroids[id])
                # Otherwise, create the list and add the current values
                except:
                    self.areas[id] = list()
                    self.centroids[id] = list()
                    self.areas[id].append(areas[id])
                    self.centroids[id].append(centroids[id])

        return self.centroids, self.areas
        
class ObjectTracker():

    # Initializes tracker
    def __init__(self, area_thresh = 0.05, window_size = 20, tolerance = float('Inf')):

        self.ptr = 0
        self.tolerance = tolerance
        self.centroids = OrderedDict()
        self.areas = OrderedDict()
        self.changed = OrderedDict()
        self.disappeared = OrderedDict()
        self.thresh = area_thresh
        self.window = window_size

    # Registers an object in the tracking list
    def register(self, centroid, area):

        self.centroids[self.ptr] = centroid
        self.areas[self.ptr] = area
        self.disappeared[self.ptr] = 0
        self.changed[self.ptr] = False
        self.ptr += 1

    # Removes an object from the tracking list
    def remove(self, id): 

        del self.centroids[id]
        del self.areas[id]
        del self.disappeared[id]
        del self.changed[id]

    # Use the bounding box coordinates to derive the centroid
    def compute_centroids(self, coord_objs):

        centroids = np.zeros((len(coord_objs), 2), dtype = 'int')

        # Loop over the bounding box rectangles [xmin ymin xmax ymax]
        for i in range(len(coord_objs)):

            # (xmin + xmax)/2
            c_x = int((coord_objs[i][0] + coord_objs[i][2]) / 2.0)
            # (ymin + ymax)/2
            c_y = int((coord_objs[i][1] + coord_objs[i][3]) / 2.0)

            # Stores centroids
            centroids[i] = (c_x, c_y)

        return centroids

    # Use the bounding box coordinates to derive the bounding boxes area
    def compute_areas(self, coord_objs):

        areas = np.zeros(len(coord_objs), dtype = float)

        # Loop over the bounding box rectangles [xmin ymin xmax ymax]
        for i in range(len(coord_objs)):

            # area = (xmax - xmin) * (ymax - ymin)
            areas[i] = (coord_objs[i][2] - coord_objs[i][0]) * (coord_objs[i][3] - coord_objs[i][1])

        return areas

    # Suppression of occurrences due to lack of expansion in the detection area
    def bbox_suppression(self, log):

        # Detections that should be suppressed
        idxs = list()

        for (id, areas) in log.areas.items():
            # Pearson's coefficient of variation: from scipy.stats import variation
            var = variation(np.array(areas[-self.window:]))
            # print(var)

            # this function works similar to variation()
            # cv = lambda x : np.std(x) / np.mean(x)
            # var = np.apply_along_axis(cv, axis = 0, arr = np.array(areas[-self.window:]))

            if var < self.thresh and self.changed[id] is False:
                idxs.append(id)
            else:
                self.changed[id] = True
            
        return idxs

    def tracking(self, coord_objs):

        # If the list of bounding boxes is empty
        if len(coord_objs) == 0:
            
            # Mark objects that did not appear in the current frame
            for id in list(self.disappeared.keys()):
                self.disappeared[id] += 1

                # If the object is missing for many frames it is removed
                if self.disappeared[id] > self.tolerance:
                    self.remove(id)

            return self.centroids, self.areas
                    
        # Compute centroids
        centroids = self.compute_centroids(coord_objs)

        # Compute areas
        areas = self.compute_areas(coord_objs)

        # There are no objects to track yet
        if len(self.centroids) == 0:
            # Registering objects found in the current frame
            for c in range(len(centroids)):
                self.register(centroids[c], areas[c])

        # Objects are already being tracked
        else:

            # List of object ids and corresponding centroids and areas
            object_ids = list(self.centroids.keys())
            object_centroids = list(self.centroids.values())
            object_areas = list(self.areas.values())

            # Compute the distance between each pair of object centroids and new centroids
            # Columns of matrix D: distance from the first element of "centroids" to all others of "object_centroids" ... 
            #D = dist.cdist(np.array(object_centroids), centroids, metric = 'euclidean') #from scipy.spatial import distance as dist
            D = np.array([[np.linalg.norm(i-j) for j in centroids] for i in np.array(object_centroids)])

            # Smallest value in each row
            # Shortest distance between each element of "object_centroids" and all elements of "centroids"
            row_min = D.min(axis = 1)
            # Sort the row indexes based on their minimum values
            rows = row_min.argsort()

            # Smallest value in each column
            # Shortest distance between each element of "centroids" and all elements of "object_centroids"
            col_min = D.argmin(axis = 1)
            # Sorting using thre previously computed row index list
            cols = col_min[rows]

            # Set of column and row indexes already examined
            usedCols = set()
            usedRows = set()

            # Loop over the combination of the index tuples
            for (row, col) in zip(rows, cols):

                # If the value has already been examined, just ignore it
                if col in usedCols or row in usedRows:
                    continue

                # Otherwise, grab the object ID for the current row
                objectID = object_ids[row]
                # Update centroid
                self.centroids[objectID] = centroids[col]
                # Update area
                self.areas[objectID] = areas[col]
                # Reset the disappeared counter
                self.disappeared[objectID] = 0

                # Adds examined column and row
                usedCols.add(col)
                usedRows.add(row)

            # Computes columns and rows that have not been examined
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)
            unusedRows = set(range(0, D.shape[0])).difference(usedRows)

            # If the number of object centroids is equal or greater than the number of current centroids
            if D.shape[0] >= D.shape[1]:

                # Check if some of these objects have potentially disappeared
                for row in unusedRows:

                    objectID = object_ids[row]
                    self.disappeared[objectID] += 1

                    # If the number of consecutive frames without the object has been extrapolated, delete it
                    if self.disappeared[objectID] > self.tolerance:
                        self.remove(objectID)


            # If the number of current centroids is greater than the number of object centroids
            else:

                # Register each new object centroid as a trackable object
                for col in unusedCols:
                    self.register(centroids[col], areas[col])

        # Return the set of trackable objects
        return self.centroids, self.areas