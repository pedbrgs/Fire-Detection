# Fire Detection

**Author:** [Pedro Vinícius A. B. Venâncio](https://www.linkedin.com/in/pedbrgs/)<sup>1</sup> <br />

> <sup>1</sup> Graduate Program in Electrical Engineering ([PPGEE](https://www.ppgee.ufmg.br/indexi.php)/[UFMG](https://ufmg.br/international-visitors))<br />

***

## About

<p align="justify"> This repository contains the models and source codes of hybrid systems for fire detection implemented during my master's degree, as well as some baseline models for comparison purposes. The proposed hybrid systems are composed of two sequential stages: (i) spatial detection, which consists of identifying and locating fire and smoke events on the scene based on spatial patterns, and (ii) temporal analysis of the events detected in the previous stage, in order to make a final decision on whether a fire is actually taking place. The baseline models are simple convolutional neural networks for fire classification proposed in the literature. </p>

## How to run a hybrid system

<p align="justify"> The first stage of the hybrid system is a YOLOv5 network (small or large) and the second stage can be a area variation technique (AVT) or a temporal persistence technique (TPT). We recommend AVT for outdoor scenes and TPT for indoor scenes. </p>

After running the system, the videos with the detections are saved in `runs/detect/exp/`.

### YOLOv5+AVT

If you want to use the hybrid system YOLOv5+AVT, run the following command:

`python detect.py --source <video_file> --weights <weights_file> --temporal tracker`

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the area variation technique by specifying the additional flags `--area-thresh` and `window-size`.

### YOLOv5+TPT

If you want to use the hybrid system YOLOv5+TPT, run the following command:

`python detect.py --source <video_file> --weights <weights_file> --temporal persistence`

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the persistence temporal technique by specifying the additional flags `--persistence-thresh` and `window-size`.

### YOLOv5

If you want to use only the YOLOv5 network, run the following command:

`python detect.py --source <video_file> --imgsz 640 --weights <weights_file>`

where `<video_file>` is the video in which you will detect fire and `<weights_file>` is the file with the network weights (can be [yolov5s.pt](https://drive.google.com/file/d/18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um/view?usp=sharing) or [yolov5l.pt](https://drive.google.com/file/d/14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS/view?usp=sharing)). You can change the parameters of the YOLOv5 network by specifying the additional flags `--img-size`, `--conf-thres` and `--iou-thres`.

## How to run a baseline model

If you want to use a baseline model, run the following command:

`python baseline.py --video <video_file> --model <model_name>`

where `<video_file>` is the video in which you will detect fire and `<model_name>` is the name of the model to be used (can be `'firenet'` or `'mobilenet'`).

## Models

Download the model weights from the root of this repository by running the `./scripts/download_models.sh` script or manually using the links below.

- [Baseline models.](https://drive.google.com/drive/folders/1jgZBi2DrfRcRKCZ9ZNdH13uHe8ckWCUJ?usp=sharing)
- [Proposed models.](https://drive.google.com/drive/folders/1s3sfGdH6ViCD1vVMgif1KQni5vUeFacT?usp=sharing)

## Dependencies

To install the dependencies, run the following command:

`pip install -r requirements.txt`

## Citation

Please cite the following paper if you use the proposed YOLOv4 models for fire and smoke detection:

- <p align="justify"><b>Pedro Vinícius Almeida Borges de Venâncio</b>, Adriano Chaves Lisboa, Adriano Vilela Barbosa: <a href="https://link.springer.com/article/10.1007/s00521-022-07467-z"> An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices. </a> In: Neural Computing and Applications, 2022.</p>

Please cite the following paper if you use FireNet for fire and smoke classification:
- <p align="justify">Arpit Jadon, Mohd. Omama, Akshay Varshney, Mohammad Samar Ansari, Rishabh Sharma: <a href="https://arxiv.org/abs/1905.11922"> FireNet: A Specialized Lightweight Fire & Smoke Detection Model for Real-Time IoT Applications. </a> In: arXiv, 2019.</p>

Please cite the following paper if you use MobileNet for fire classification:
- <p align="justify">Debajyoti Mukhopadhyay, Ramya Iyer, Sagarika Kadam, Rakshanda Koli: <a href="https://ieeexplore.ieee.org/document/8978439"> FPGA Deployable Fire Detection Model for Real-Time Video Surveillance Systems Using Convolutional Neural Networks. </a> In: IEEE Global Conference for Advancement in Technology (GCAT), 2019, Bangalore, India.</p>

## References

- [D-Fire dataset.](https://github.com/gaiasd/DFireDataset)
- [FireNet dataset.](https://drive.google.com/drive/folders/1HznoBFEd6yjaLFlSmkUGARwCUzzG4whq?usp=sharing)
- [Foggia's dataset.](https://mivia.unisa.it/datasets/video-analysis-datasets/fire-detection-dataset/)
- [YOLOv4 with Darknet.](https://github.com/AlexeyAB/darknet)
- [YOLOv5 with PyTorch.](https://github.com/ultralytics/yolov5)
- [Simple object tracking with OpenCV.](https://pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/)
- [Inferno fire detection using CNNs.](https://github.com/bubblebeam/Inferno-Realtime-Fire-detection-using-CNNs)
- [FireNet lightweight network for fire detection.](https://github.com/arpit-jadon/FireNet-LightWeight-Network-for-Fire-Detection)
