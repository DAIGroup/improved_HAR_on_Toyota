# Improved action recognition with Separable spatio-temporal attention using alternative Skeletal and Video pre-processing
**Pau Climent-Pérez · Francisco Flórez-Revuelta**

MDPI Sensors, 2021 _(accepted)_

**Abstract:** The potential benefits of recognising activities of daily living from video for active and assisted living
have yet to be fully untapped. These technologies can be used for behaviour understanding, and lifelogging for
caregivers and end users alike. The recent publication of realistic datasets for this purpose, such as the
Toyota Smarthomes dataset calls for pushing forward the efforts to improve action recognition. Using the separable
spatio-temporal attention network proposed in the literature, this paper introduces a series of pre-processing methods
for skeletal pose data and RGB crops that improves the baseline results by 9.5% (on the cross-subject experiments),
outperforming state-of-the-art techniques in this field when using the original unmodified skeletal data in dataset.

## Involved repositories

The experiments in this paper have been carried out using the following repositories in this GitHub account:

* https://github.com/DAIGroup/mask_rcnn
* https://github.com/DAIGroup/i3d
* https://github.com/DAIGroup/LSTM_action_recognition
* https://github.com/DAIGroup/separable_STA

You can read more about them on their respective `README.md` files.

## Available downloads

* Please see `DAIGroup/LSTM_action_recognition` to download pre-processed rotated skeletons.
* Please visit `DAIGroup/mask_rcnn` to download pre-processed Mask RCNN bounding box data.

## Reproducibility

### Step 1: Obtain Mask RCNN detections

The repository `DAIGroup/mask_rcnn` contains a Mask RCNN implementation that is used to detect human bounding boxes for
the Toyota dataset.

### Step 2: I3D net training for action recognition

`DAIGroup/i3d` contains a `preprocessing/` folder with scripts to further _pre-process_ the detections obtained in
Step 1 (i.e. to fill the gaps in detected bounding boxes), as well as to create the crops used for training.

These crops can be extracted from the images in two forms: 1) _normal_, or one crop per frame; or 2) as a _full crop_
of the whole activity, as described in our paper (Climent-Pérez et al. 2021).

The network can then be trained for action recognition, as usual. The layer before the Global Average Pooling (GAP) 
is used in Step 4 below, as described in (Das et al. 2019).

### Step 3: LSTM training for action recognition

`DAIGroup/LSTM_action_recognition` is a 3-layer LSTM network that can be trained for action recognition first, and then
used in the next step (Step 4), to assist the attention block. 

### Step 4: STA block (joint) training

`DAIGroup/separable_STA` is a project consisting in the implementation of the attention block described in
(Das et al. 2019). It loads the weights `.hdf5` files from both branches above (LSTM, Step 3; and I3D, Step 2). 
It can be trained _jointly_ with the I3D branch (left as _trainable_ for fine tuning). The LSTM branch, however, is left
_frozen_ and used to assist the attention block in _modulating_ the convolutional feature map output of I3D.

## Report generation

The script provided with this repository is used to generate reports about the results obtained.
Each project in Steps 2-4 contains an _evaluate_ script (i.e. `lstm_evaluate.py`, `i3d_evaluate.py`,
and `sta_evaluate.py`). These generate `.csv` files containing confusion matrices that the `generate_report.py` then
draws and saves as `.pdf` images. Mean average per class accuracy as well as overall classification accuracy are
also calculated. 

### Supplemental material: confusion matrices for all results

The `results/` directory contains pre-drawn confusion matrices for all results reported in the paper.
If using in your own materials, please cite (Climent-Pérez et al. 2021).

## References

* **(Das et al. 2019)** Das, S., Dai, R., Koperski, M., Minciullo, L., Garattoni, L., Bremond, F., & Francesca, G. (2019). Toyota smarthome: Real-world activities of daily living. In Proceedings of the IEEE International Conference on Computer Vision (pp. 833-842).
* **(Climent-Pérez et al. 2021)** Climent-Pérez, P., Florez-Revuelta, F. (2021). Improved action recognition with Separable spatio-temporalattention using alternative Skeletal and Video pre-processing, Sensors, _accepted_.
