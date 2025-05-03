# :fire: Fire Detection

**Author:** [Pedro Vinícius A. B. Venâncio](https://www.linkedin.com/in/pedbrgs/)<sup>1</sup> <br />

> <sup>1</sup> Graduate Program in Electrical Engineering ([PPGEE](https://www.ppgee.ufmg.br/indexi.php)/[UFMG](https://ufmg.br/international-visitors))<br />

***

# :book: About

<p align="justify"> This repository contains source code and models developed during my master's research on hybrid fire and smoke detection systems, along with baseline models for comparison.

The proposed hybrid systems are composed of two sequential stages:

1. **Spatial Detection** — identifies and locates fire/smoke events using spatial patterns.
2. **Temporal Analysis** — verifies whether a fire event is truly taking place based on temporal behavior of detected regions.

Baseline models are standard convolutional neural networks (CNNs) proposed in the literature for fire classification.
</p>

# :high_brightness: Quickstart

## :open_file_folder: 1. Prepare your environment

1. Clone the repository and place your input videos in the `examples/` folder. 

2. Build the Docker image:
```bash
docker build -t fire-detection .
```

3. Run the container:
```bash
docker run -it --rm fire-detection /bin/bash
```

## :snowflake: 2. Choose a fire detection system

Select one of the detection methods below and follow its respective instructions.

### :wrench: Detection using a hybrid system

The hybrid detection system combines two stages:

- **Stage 1:** A YOLOv5 network (`small` or `large`) to identify candidate fire/smoke regions in each frame.
- **Stage 2:** A temporal analysis method to confirm true fire events:
  - **AVT (Area Variation Technique):** recommended for **outdoor** scenes.
  - **TPT (Temporal Persistence Technique):** recommended for **indoor** scenes.

Detections are saved to `runs/detect/exp/`.

#### :orange_circle: YOLOv5+AVT

If you want to use the hybrid system YOLOv5+AVT, run the following command inside the container:
```bash
python detect.py --source <video_file> --weights ./weights/<weights_file> --temporal tracker
```

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the area variation technique by specifying the additional flags `--area-thresh` and `window-size`.

#### :red_circle: YOLOv5+TPT

If you want to use the hybrid system YOLOv5+TPT, run the following command inside the container:
```bash
python detect.py --source <video_file> --weights ./weights/<weights_file> --temporal persistence
```

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the persistence temporal technique by specifying the additional flags `--persistence-thresh` and `window-size`.

### :wrench: Detection using YOLOv5 only

To run only the YOLOv5 network without temporal analysis, use:
```bash
python detect.py --source <video_file> --imgsz 640 --weights ./weights/<weights_file>
```

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the YOLOv5 network by specifying the additional flags `--img-size`, `--conf-thres` and `--iou-thres`.

### :wrench: Detection using baseline models

If you want to use a baseline model, run the following command inside the container:
```bash
python baseline.py --video <video_file> --model <model_name>
```

where `<video_file>` is the video in which you will detect fire and `<model_name>` is the name of the model to be used (can be `'firenet'` or `'mobilenet'`).

# :floppy_disk: Model weights

Run the script to fetch all model weights:

```bash
./scripts/download_models.sh
```

Or download manually:

- [Baseline models.](https://drive.google.com/drive/folders/1jgZBi2DrfRcRKCZ9ZNdH13uHe8ckWCUJ?usp=sharing)
- [Proposed models.](https://drive.google.com/drive/folders/1s3sfGdH6ViCD1vVMgif1KQni5vUeFacT?usp=sharing)

# :scroll: Citation

Please cite the following paper if you use our proposed hybrid systems for fire and smoke detection:

- <p align="justify"><b>Pedro Vinícius Almeida Borges de Venâncio</b>, Roger Júnio Campos, Tamires Martins Rezende, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-023-08260-2"> A hybrid method for fire detection based on spatial and temporal patterns. </a> In: Neural Computing and Applications, 2023.</p>

If you use our YOLOv4 models for fire and smoke detection, please cite the following paper:

- <p align="justify"><b>Pedro Vinícius Almeida Borges de Venâncio</b>, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-022-07467-z"> An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices. </a> In: Neural Computing and Applications, 2022.</p>

# :books: References

- YOLO models: [YOLOv4 (Darknet)](https://github.com/AlexeyAB/darknet), [YOLOv5 (PyTorch)](https://github.com/ultralytics/yolov5)
- Object tracking: [OpenCV Tracker (PyImageSearch)](https://pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/).
- Baseline models: [Inferno CNN](https://github.com/bubblebeam/Inferno-Realtime-Fire-detection-using-CNNs), and [FireNet](https://github.com/arpit-jadon/FireNet-LightWeight-Network-for-Fire-Detection).
- Datasets: [D-Fire dataset](https://github.com/gaiasd/DFireDataset), [FireNet dataset](https://drive.google.com/drive/folders/1HznoBFEd6yjaLFlSmkUGARwCUzzG4whq?usp=sharing), and [Foggia's dataset](https://mivia.unisa.it/datasets/video-analysis-datasets/fire-detection-dataset/).
