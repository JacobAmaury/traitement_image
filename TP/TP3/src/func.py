#*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 14102025 15:48:48     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
from scipy.ndimage import laplace
import cv2




def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img
import numpy as np


def contrast_image(image_path):
    image = open_image(image_path)
    image_grey = open_image(image_path, "L")
    contrast_image = np.abs(laplace(image_grey))

    return contrast_image, image


def refocus(path_images):
    contrasts = []
    images = []
    for path in path_images:
        contrast, image = contrast_image(path)
        contrasts.append(contrast)
        images.append(image)

    contrasts = np.stack(contrasts)
    images = np.stack(images) # creat an array of 3 images, x, y, rgb

    best_image = np.argmax(contrasts, axis=0) # best image
    new_image = np.zeros_like(images[0])
    h, w, c = images[0].shape 
    for y in range(h):
        for x in range(w):
            new_image[y,x,:] = images[best_image[y,x],y,x,:]

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
    h, w = energy.shape
    coords = np.empty((h,w), dtype=object) 
    sum_energys = np.zeros(w)
    
    for y in range(1,h-1):
        for x in range(1,w-1):
            neighbors = [
                (energy[y+1, x-1], (y+1, x-1)),
                (energy[y+1, x],   (y+1, x)),
                (energy[y+1, x+1], (y+1, x+1))]
            
            min_energy = 1e10
            min_coord = 0
            for i in range(3):
                min_energy_act, min_coord_act = neighbors[i]
                if min_energy_act < min_energy:
                    min_energy = min_energy_act
                    min_coord = min_coord_act
                
                 
            sum_energys[x] += min_energy
            coords[y, x] = min_coord
            
    index_opt = np.argmin(sum_energys)
    optimal_coords = [coords[y, index_opt] for y in range(h) if coords[y, index_opt] is not None]
    sum_min_energy = sum_energys[index_opt]

    return energy, coords, sum_energys, optimal_coords, sum_min_energy