import os
import numpy as np
import rasterio

# use the function to create folders for storage of specific categories of images inside the index dataset

def mkd(output, i):
    dir = os.path.join(output, i)
    os.makedirs(dir)


# set the path to the directory containing the EuroSAT dataset
data_dir = '.../EuroSAT_MS/EuroSAT_MS'

# set the path to the directory where the npy files will be saved
output_dir = '.../IndiexName'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# define a list of the class names in the dataset
class_names = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
               'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']
# loop over each class
for i in range(len(class_names)):


# get the name of the current class
    class_name = class_names[i]
    mkd(output_dir, class_name)
    output_path1 = os.path.join(output_dir, class_name)
    # set the path to the directory containing the images for the current class
    class_dir = os.path.join(data_dir, class_name)

    # get a list of the filenames of the images for the current class
    image_filenames = os.listdir(class_dir)
    for j in range(len(image_filenames)):
        image_filename = image_filenames[j]
        image_path = os.path.join(class_dir, image_filename)
        with rasterio.open(image_path) as src:
            # channels that we have used
            bands = src.read()
            blue_band = bands[1]
            green_band = bands[2]
            red_band = bands[3]
            nir_band = bands[7]
            swir_band1 = bands[11]

            # define default values
            s = 0.33
            a = 0.5
            X = 1.5
            L = 1
            # L = 0.33
            # process calculation to indices, calculation for TSAVI is shown, for other indices just type the formula to generate indices we need
            result_band = (s*(nir_band-s*red_band-a))/(a*nir_band+red_band-a*s+X * (1+s*s))
            # Add the result of the calculation as a new channel to the bands
            bands = np.vstack((bands, result_band[np.newaxis, :]))
            # write our result to the output folder
            output_filepath = os.path.join(output_path1, image_filename)
            with rasterio.open(output_filepath, 'w', driver='GTiff', height=src.height, width=src.width,
                               count=bands.shape[0], dtype=bands.dtype, transform=rasterio.Affine.identity()) as dst:
                dst.write(bands)


