import os
import cv2
import time
from tensorflow import keras
import argparse
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

"""
FireNet from:
Jadon, A., Omama, M., Varshney, A., Ansari, M. S., & Sharma, R. (2019).
FireNet: a specialized lightweight fire & smoke detection model for
real-time IoT applications. arXiv preprint arXiv:1905.11922.
"""

"""
MobileNet from:
Mukhopadhyay, D., Iyer, R., Kadam, S., & Koli, R. (2019).
FPGA Deployable Fire Detection Model for Real-Time Video Surveillance
Systems Using Convolutional Neural Networks. In 2019 Global Conference for
Advancement in Technology (GCAT) (pp. 1-7). IEEE.
"""

def run_baseline(model_name, video_path):

    classes = ['fire', 'non_fire']
    detected = False
    video = video_path.split('/')[-1]
    
    if model_name.lower() == 'firenet':
        img_size = 64
    elif model_name.lower() == 'mobilenet':
        img_size = 224

    # Loading the trained fire classification model
    model = load_model(model_name+'.h5')
    cap = cv2.VideoCapture(video_path)
    time.sleep(2)
    # try to get the first frame
    if cap.isOpened():
        rval, frame = cap.read()
    else:
        rval = False
    
    # i-th frame
    frame = 0
    first_frame = np.nan
    # list of time detections
    time_list = list()

    while(1):

        rval, image = cap.read()
        if rval==True:

            # Increases number of frames
            frame += 1
            # Preprocessing image according to the model
            image = cv2.resize(image, (img_size, img_size))
            if model_name.lower() == 'firenet':
                image = image.astype("float") / 255.0
            elif model_name.lower() == 'mobilenet':
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            if model_name.lower() == 'mobilenet':
                image = keras.applications.mobilenet.preprocess_input(image)

            tic = time.time()
            # Inference
            softmax_output = model.predict(image)
            toc = time.time()
            det_time = toc - tic
            print("Time taken = ", det_time)
            time_list.append(det_time)

            # Output prediction from softmax
            idx = np.argmax(softmax_output)
            prediction = classes[idx]
            print(f"Prediction: {prediction}")
            if prediction.lower() == 'fire':
                if detected == False:
                    first_frame = frame
                detected = True

        elif rval==False:
                break
    end = time.time()

    cap.release()
    cv2.destroyAllWindows()

    output = pd.DataFrame({'video': [video],
                           'network': [model_name],
                           'detected': [detected],
                           'first_frame': [first_frame],
                           'time_avg': [np.mean(time_list)]})

    return output

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type = str, help = 'video')
    parser.add_argument('--model', type = str, help = 'model name (e.g., mobilenet, firenet)')
    params = parser.parse_args()

    # Run inference
    result = run_baseline(model_name = params.model,
                          video_path = params.video)
    print("Results")
    print(result)
