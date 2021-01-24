## Predicting Vehicle Collisions using Data Collected from Video Games
### [Tensorflow](https://github.com/gnsrla12/predicting-vehicle-collisions-using-data-collected-from-video-games)

<p align="center">
  <img src="movie.gif">
</p>

## Getting Started
### Installation
- Install tensorflow
- Clone this repo:
```bash
git clone https://github.com/gnsrla12/predicting_vehicle_collsiions_using_data_collected_from_video_game
cd predicting_vehicle_collsiions_using_data_collected_from_video_game
```

### Prepare Dataset
- Download YouTubeCrash (Real accident dataset collected from YouTube):
```
python ./datasets/download_ytcrash.py
```
- Download GTACrash (Synthetic accident dataset collected from Grand Theft Auto V):
```bash
python ./datasets/download_gtacrash.py
```
You can skip downloading GTACrash if you just want to apply pretrained model to YouTubeCrash.

### Apply a Pre-trained Model
- Download the pre-trained model trained on GTACrash with refined labels:
```
python ./checkpoints/download_model.py
```
- Now, let's measure performance of our model on the YouTube test dataset:
```
python ./scripts/test_script.py
```
The test results will be printed. ROC-AUC should output 0.915411. (Note that the measured accuracy is when threshold of the predictor is fixed at 0.5, and that is not an appropriate metric for the binary classification task)

- Finally, visualize the prediction results of the pretrained model:
```bash
python ./scripts/visualize_script.py
```
The visualized results will be saved to : `./visualization/`

### Train
- Train a model on the GTACrash dataset with refined labels (Trained model overwrites the existing pre-trained model):
```bash
python ./scripts/train_gta_script.py
```

- Train a model on the YouTubeCrash dataset:
```bash
python ./scripts/train_yt_script.py
```

The trained model will be saved to: `./checkpoints/`

