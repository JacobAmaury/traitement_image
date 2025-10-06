#/*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 03102025 08:47:48     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random as rd
from skimage.transform import resize

def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img

def conv_product(image, filter, im_type="RGB"):
    if(im_type == "RGB"):
        height, width, channels = image.shape
        filter_height, filter_width = filter.shape
        to_border = int(filter_height/2)

        im_convo = np.zeros_like(image)

        #normalistion du filtre
        sum_coef = np.sum(filter)
        if sum_coef == 0: sum_coef = 1


        for c in range(channels):
            for y in range(to_border, height - to_border): #evite les effets de bord
                for x in range(to_border, width - to_border):
                    #on récupere la fentre autour du point(x,y)
                    conv = image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1, c]
                    value = np.sum(conv * filter) / sum_coef #on fait la somme et on normalise

                    val = int(value)
                    if val < 0: val = 0
                    elif val > 255: val = 255

                    im_convo[y, x, c] = val
    else: 

        height, width = image.shape
        filter_height, filter_width = filter.shape
        to_border = int(filter_height/2)

        im_convo = np.zeros_like(image)

        #normalistion du filtre
        sum_coef = np.sum(filter)
        if sum_coef == 0: sum_coef = 1


            
        for y in range(to_border, height - to_border): #evite les effets de bord
            for x in range(to_border, width - to_border):
                #on récupere la fentre autour du point(x,y)
                conv = image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1]
                value = np.sum(conv * filter) / sum_coef #on fait la somme et on normalise

                val = int(value)
                if val < 0: val = 0
                elif val > 255: val = 255

                im_convo[y, x] = val

    return im_convo

def median(image, window_size, type_im):
    if(type_im == "RGB"): #
            
        height, width, channels = image.shape
        to_border = int(window_size/2)

        im_med = np.zeros_like(image) #creat an array of the same size as the image

        for c in range(channels):
            for y in range(to_border, height - to_border): #evite les effets de bord
                for x in range(to_border, width - to_border):
                    #compute the median
                    median = np.median(image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1, c])

                    im_med[y, x, c] = median
    else:# same thing but for gray scale 
        height, width = image.shape
        to_border = int(window_size/2)

        im_med = np.zeros_like(image)

        for y in range(to_border, height - to_border): #evite les effets de bord
            for x in range(to_border, width - to_border):
                median = np.median(image[y - to_border : y + to_border + 1, x - to_border : x + to_border + 1])

                im_med[y, x] = median
        
    return im_med



def poivre_sel(image, prob):
    """Prob should be between 0 and 1"""
    width, height, chanel = image.shape
    noisy_image = np.zeros_like(image)
    
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            random_value = rd.random()
            if(random_value < prob):
                noisy_image[x-1:x+1, y-1:y+1, :] = 255 #put a square of white pixels
            else:
                noisy_image[x-1:x+1, y-1:y+1, :] = image[x-1:x+1, y-1:y+1, :] 
            
            
            
    return noisy_image.astype(int) 

def fft_im(image):
    return np.fft.fft2(image)



def print_fft(image):
    fft = np.fft.fft2(image)
    fft_shift = np.fft.fftshift(fft)
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(np.log(np.abs(fft_shift)), cmap='gray')
    plt.show()
    

def crop_image(image_to_crop, dimensions):
    x, y, _ = image_to_crop.shape 
    center_x = x // 2
    center_y = y // 2
    
    crop_image = image_to_crop[
        center_x - dimensions[0]//2 : center_x + dimensions[0]//2,
        center_y-1 - dimensions[1]//2 : center_y + dimensions[1]//2]
    return crop_image 
    
def picture_flag(image, flag):
    image = image.astype(np.uint8)
    image = Image.fromarray(image)

    flag = flag.astype(np.uint8)
    flag = Image.fromarray(flag)
    flag = flag.resize(image.size)

    result = ((np.array(image).astype(int) + np.array(flag).astype(int)) / 2)
    return result.astype(int)

def normalisation_histo(image):
    I_max = np.max(image)
    I_min = np.min(image)
    return (((image-I_min)/(I_max-I_min))*255).astype(int)


def histo_cumu(image):
    histo, bin = np.histogram(image, 256)
    histo_cumu = np.zeros_like(histo)
    for i in range(histo.shape[0]):
        histo_cumu[i] = np.sum(histo[:i+1])

    return histo_cumu
    

def equa_histo(image):
    histo_cumu1 = histo_cumu(image)
    histo_cumu_normalized = histo_cumu1 * 255 / histo_cumu1[-1]
    LUT = histo_cumu_normalized.astype(np.uint8)

    return LUT[image]


def equlisation_exact(image):
    
    im_ligne = image.reshape(-1) #met l'image en vecteur ligne
    
    im_ligne_sorted = np.argsort(im_ligne) 
    
    uniform_value = np.linspace(0,255,im_ligne_sorted.shape[0])
    im_ligne[im_ligne_sorted] = uniform_value
    equalized_image = im_ligne.reshape(image.shape).astype(int)
    return equalized_image

def thresholding(image, threshold):
    im_thresh = np.zeros_like(image)
    for y in range(image.shape[1]):
        for x in range(image.shape[0]):
            if image[x,y] > threshold :
                im_thresh[x,y] = 255
            else: im_thresh[x,y] = 0
    return im_thresh

    
def dilatation(im):
    img = im / 255
    result = np.zeros_like(img)
    
    structural_element = np.array([[0,1,0],
                                   [1,1,1],
                                   [0,1,0]])
    
    for x in range(1, img.shape[0]-1):
        for y in range(1, img.shape[1]-1):
            actual_point = img[x-1:x+2, y-1:y+2]  
            if np.sum(actual_point * structural_element) > 0:
                result[x, y] = 1
    
    return (result * 255)


def erosion(im):
    img = im / 255
    result = np.zeros_like(img)
    
    structural_element = np.array([[0,1,0],
                                   [1,1,1],
                                   [0,1,0]])
    
    for x in range(1, img.shape[0]-1):
        for y in range(1, img.shape[1]-1):
            actual_point = img[x-1:x+2, y-1:y+2]  
            if np.sum(actual_point * structural_element) == 5:
                result[x, y] = 1
    
    return (result * 255)


def zone_equa_histo(image, num_bloc):
    width, height = image.shape #Only gray scale image
    zone_equa_image = np.zeros_like(image)
    step_x = width//num_bloc
    step_y = height//num_bloc
    for y in range(0,height, step_y):
        for x in range(0, width, step_x):
                    
            histo_cumu1 = histo_cumu(image[x:x+step_x, y:y+step_y])
            histo_cumu_normalized = histo_cumu1 * 255 / histo_cumu1[-1]
            LUT = histo_cumu_normalized.astype(np.uint8)
            zone_equa_image[x:x+(step_x), y:y+(step_y)] = LUT[image[x:x+step_x, y:y+step_y]]
    return zone_equa_image


