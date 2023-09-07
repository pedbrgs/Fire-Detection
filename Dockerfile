# Start from Python 3.8 image
FROM silverlogic/python3.8
# Create working directory
WORKDIR /fire-detection/
# Copy requirements
COPY requirements.txt .
# Install requirements
RUN pip install --no-cache-dir -r requirements.txt
# Copy source-code
COPY . .
# Download trained models
RUN mkdir ./weights/
RUN ./scripts/download_models.sh
RUN mv yolov5l.pt ./weights/
RUN mv yolov5s.pt ./weights/
RUN mv mobilenet.h5 ./weights/
RUN mv firenet.h5 ./weights/