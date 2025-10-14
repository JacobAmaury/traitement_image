#*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 14102025 15:48:48     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
from skimage.feature import match_descriptors, plot_matched_features, SIFT
from skimage.feature import match_descriptors
from skimage import io, color
import cv2



def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img
import numpy as np

def refocus(image_1, image_2, image_3):
    h, w, c = image_1.shape
    new_image = np.zeros_like(image_1)
    
    new_image[:125,:,:] = image_3[:125,:,:]
    new_image[125:200,:,:] = image_2[125:200,:,:]
    new_image[200:h,:,:] = image_1[200:h,:,:] 
    return new_image

def energy_map_sobel(img):
    gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]

    h, w = gray.shape

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])

    padded = np.pad(gray, ((1, 1), (1, 1)), mode='edge')
    Gx = np.zeros_like(gray)
    Gy = np.zeros_like(gray)

    for i in range(h):
        for j in range(w):
            region = padded[i:i+3, j:j+3]
            Gx[i, j] = np.sum(region * sobel_x)
            Gy[i, j] = np.sum(region * sobel_y)

    energy = np.sqrt(Gx**2 + Gy**2)
    energy = (energy - energy.min()) / (energy.max() - energy.min())

    return energy

def min_path(img):
    energy = energy_map_sobel(img)
    w, h = energy.shape
    x_start = 0
    coord_min = []
    for x in range(w):
        test = energy[0,x] + energy[1,x]
        if test > energy:
            energy=test 
    
    