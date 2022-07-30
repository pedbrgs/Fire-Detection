# !/bin/bash

# YOLOv4
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=16Eq8WiSGeUUWC-C_zlS3ZY8XM4d_S0yr' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=16Eq8WiSGeUUWC-C_zlS3ZY8XM4d_S0yr" -O yolov4.weights && rm -rf /tmp/cookies.txt
# Tiny YOLOv4
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=17TlIiQXH8PUbeinjryAG5Lj99lCotIlm' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=17TlIiQXH8PUbeinjryAG5Lj99lCotIlm" -O tiny-yolov4.weights && rm -rf /tmp/cookies.txt
# YOLOv5 large (YOLOv5l)
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=14Qhxvruf3cVxZE_e_6tJNCA3w1xzaWQS" -O yolov5l.pt && rm -rf /tmp/cookies.txt
# YOLOv5 small (YOLOv5s)
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=18kwwGYs0CPVvrLwz283v8IXSeTrTE-Um" -O yolov5s.pt && rm -rf /tmp/cookies.txt
# MobileNet
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1x0RjMu5QaaBOl06_amcOCO2-S1kjp2lu' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1x0RjMu5QaaBOl06_amcOCO2-S1kjp2lu" -O mobilenet.h5 && rm -rf /tmp/cookies.txt
# FireNet
wget --no-check-certificate --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1XG-9olRZoBzY3riXdieqV4LmX9HXOejr' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1XG-9olRZoBzY3riXdieqV4LmX9HXOejr" -O firenet.h5 && rm -rf /tmp/cookies.txt
