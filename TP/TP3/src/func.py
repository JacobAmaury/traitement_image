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


from scipy import ndimage

#question 3 was done using this source https://andrewdcampbell.github.io/seam-carving
def energy_map_sobel(img):
    gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]

    Gy, Gx = np.gradient(gray)
    energy = np.sqrt(Gx**2 + Gy**2)
    energy = (energy - energy.min()) / (energy.max() - energy.min())

    return energy

def min_paths(img):
    energys = energy_map_sobel(img)
    h, w = energys.shape

    cumul_energys = np.zeros_like(energys)
    cumul_energys[0,:] = energys[0,:] #initialisation
    
    for i in range(1,h):
        for j in range(w):
            #we do this in order to read the energy image only once
            energys_upper = np.empty(3)
            if j>0 and j<w-1:
                energys_upper = np.array([cumul_energys[i-1,j-1], cumul_energys[i-1,j], cumul_energys[i-1,j+1]])
            elif j == 0: 
                energys_upper = np.array([np.inf, cumul_energys[i-1,j], cumul_energys[i-1,j+1]])
            elif j == w-1: 
                energys_upper = np.array([cumul_energys[i-1,j-1], cumul_energys[i-1,j], np.inf])
            cumul_energys[i,j] = energys[i,j] + np.min(energys_upper)
    
    return cumul_energys

def seam_carving(img):
    cumul_energys = min_paths(img)
    h, w = cumul_energys.shape
    new_image = np.zeros((h,w-1,3), dtype=img.dtype) #RGB
    j_min = np.argmin(cumul_energys[h-1,:])
    
    for i in range(h-1, 0, -1): 
        energys_upper = np.empty(3)
        if j_min>0 and j_min<w-1:
            energys_upper = [cumul_energys[i-1,j_min-1], cumul_energys[i-1,j_min],cumul_energys[i-1,j_min+1]]
        elif j_min == 0: 
            energys_upper = [np.inf, cumul_energys[i-1,j_min],cumul_energys[i-1,j_min+1]]
        elif j_min == w-1: 
            energys_upper = [cumul_energys[i-1,j_min-1], cumul_energys[i-1,j_min],np.inf]
        
        new_image[i,:,:] = np.delete(img[i,:,:], j_min, axis=0)     
        offset = np.argmin(energys_upper)-1 #-1, 0 or 1
        j_min += offset
        
    
    
    return new_image

from scipy.ndimage import gaussian_filter

def focus_center(img, center_width, off_center):
    h, w, _ = img.shape
    center = w//2 - off_center
    mask = img.copy()
    mask[:,center-center_width//2:center+center_width//2,:] = 0 #add black border kinda pretty
    mask = gaussian_filter(mask,sigma=(1, 1, 0))
    mask[:,center-center_width//2:center+center_width//2,:] = img[:,center-center_width//2:center+center_width//2,:]
    return mask



def focus_two_zones(img,
                    zone1_center, zone1_width, z1_top, z1_bottom,
                    zone2_center, zone2_width, z2_top, z2_bottom):

    h, w, _ = img.shape

    blur_light = gaussian_filter(img, sigma=(2, 2, 0))
    blur_strong = gaussian_filter(img, sigma=(8, 8, 0))

    mask = blur_strong.copy()

    center2 = int(w * zone2_center)
    w2 = int(w * zone2_width / 2)
    top2 = int(h * z2_top)
    bottom2 = int(h * z2_bottom)
    mask[top2:bottom2, center2 - w2:center2 + w2, :] = blur_light[top2:bottom2, center2 - w2:center2 + w2, :]

    center1 = int(w * zone1_center)
    w1 = int(w * zone1_width / 2)
    top1 = int(h * z1_top)
    bottom1 = int(h * z1_bottom)
    mask[top1:bottom1, center1 - w1:center1 + w1, :] = img[top1:bottom1, center1 - w1:center1 + w1, :]

    return mask
