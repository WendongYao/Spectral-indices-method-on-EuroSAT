import os
import numpy as np
import rasterio
# The program is modified from the original program provided by the user @tejasri19, please see https://github.com/tejasri19/EuroSAT_data_analysis/blob/main/image_to_numpy.py for original code
# set the path to the directory containing the EuroSAT dataset
data_dir = '.../IndexName'

# set the path to the directory where the npy files will be saved
output_dir = '.../folderName'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# define a list of the class names in the dataset
class_names = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
               'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']

# loop over each class
for i in range(len(class_names)):
    # get the name of the current class
    class_name = class_names[i]

    # set the path to the directory containing the images for the current class
    class_dir = os.path.join(data_dir, class_name)

    # get a list of the filenames of the images for the current class
    image_filenames = os.listdir(class_dir)

    # initialize an empty array to hold the image data
    # "64,64" represent for the size of image is 64x64
    # 1 represents 1 channel will be applied to the numpy dataset. For the grneration to multiple channels, please change the number to number of channels needed.
    X = np.zeros((len(image_filenames), 64, 64, 1))

    # loop over each image in the current class
    for j in range(len(image_filenames)):
        # get the filename of the current image
        image_filename = image_filenames[j]

        # set the path to the current image
        image_path = os.path.join(class_dir, image_filename)

        # open the image using rasterio
        with rasterio.open(image_path) as src:
            # read the image data as a numpy array
            image = src.read()
        
        # Extract the specific channel you want
        # Channels are 0-based, so 14th channel is at index 13, you can add more channels if you want to use multi-spectral method

        # Transpose the image data to the shape (len(selected_channels), 64, 64)
        selected_channels = [13]

        image = np.transpose(image[selected_channels], (1, 2, 0))

        # Add the image data to the X array
        X[j, :, :, :] = image

    # save the X array as an npy file
    np.save(os.path.join(output_dir, f'X{i}.npy'), X)

    # create an array of labels for the current class
    y = np.ones(len(image_filenames)) * i

    # save the y array as an npy file
    np.save(os.path.join(output_dir, f'y{i}.npy'), y)
