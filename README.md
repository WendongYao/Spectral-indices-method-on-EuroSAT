# Spectral-indices-method-on-EuroSAT -- Instructions
This project represents programs that are being used in the experiment of paper named with "Optimizing Remote Sensing Image Classification with Spectral Indices and Convolutional Neural Networks". Programs with different functions have been stored in separate directories, which will be introduced below.
## Generation for indices
The folder contains "IndicesDataset.py" file. This program shows first step of the experiment. The indices have been generated using the program, and stored as channels to image datasets.
## Data_Processing
The folder contains "image to numpy.py" file. This program shows second step of the experiment. The generated datasets have been reformed to numpy form using the program, being ready to be trained on ResNet models.
## ResNetTraining
The folder contains "ResNet152.ipynb" and "ResNet50.ipynb" file. This program shows third step of the experiment. The programs shows details of how the ResNet models are used to train reformed datasets.


