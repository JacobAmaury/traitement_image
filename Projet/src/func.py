import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
from scipy.ndimage import laplace
import cv2 as cv

def open_image(path, mode="RGB"):
    """Take the path of the image and the mode of the return image
        return an image wich is an np.array"""
    img = np.array(Image.open(path).convert(mode), int)
    return img

def pretreatment(image):
    """In this function we normalize and denoise the image"""
    image = image/np.max(image)
    image = cv.GaussianBlur(image,(3,3),0)
    return image

def p_tild(image ,mode=0, alpha=50, sigma=1.0, omega=0.05):
    """This function compute p_tild. if mode = 0 P = exp(-alpha * g^2) else P = 1 / (1 + (g/sigma)^2)"""
    Gy, Gx = np.gradient(image)
    g = np.sqrt(Gx**2 + Gy**2)

    p = np.empty_like(image)
    if mode == 0 :
        p = np.exp(-alpha*(g**2))
    else:
        p = 1/(1+(g/sigma)**2)
    p_tild = omega + p

    return p_tild
    
def fast_marching(P_tild, init_point_x,init_point_y):
    """This function compute the fast marching matching methode. 
        take P_tild (can be compute with the functio P_tild) and the coordinate of the initial point"""
    #initilisation
    Us = np.empty_like(P_tild)
    Us = np.inf
    Us[init_point_y, init_point_x] = 0

    labels = np.empty_like(P_tild) #FAR=0, TRIAL=1 and ALIVE = 2 
    labels = 0 
    labels[init_point_y, init_point_x] = 1

    TRIAL_pixels = [(init_point_y, init_point_x)] #list of trial points




    while len(TRIAL_pixels) != 0:


