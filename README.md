# Deepfake Detection Web App

This project is a web app that detects deepfake videos by analyzing facial features and motion across frames. It uses deep learning models to spot inconsistencies in face movement that are common in AI-generated videos.

# What It Does

- Takes a short video as input
- Extracts individual frames
- Uses a CNN (InceptionV3) to understand facial features
- Passes those features through LSTM and GRU layers to detect unnatural motion patterns
- Predicts whether the video is real or fake

## Model Overview

- InceptionV3 is used for feature extraction from individual video frames
- A combination of LSTM and GRU layers helps in analyzing the sequence of frames
- Final prediction layer outputs a probability of the video being real or fake
