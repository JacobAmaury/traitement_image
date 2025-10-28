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



def is_pix(x, y, max_x, max_y):

    if x >= 0 and x < max_x and y >= 0 and y < max_y:
        return 1
    return 0

def pix_neighbours(x, y, max_x, max_y):

    neighbours = []
    if is_pix(x-1,y, max_x, max_y): neighbours.append((y,x-1))
    if is_pix(x+1,y, max_x, max_y): neighbours.append((y,x+1))
    if is_pix(x,y-1, max_x, max_y): neighbours.append((y-1,x))
    if is_pix(x,y+1, max_x, max_y): neighbours.append((y+1,x))
    return neighbours

def solve_eikonal(Us, pix_y, pix_x, P_tilds):
    return 0

def fast_marching(P_tilds, init_point_x,init_point_y):
    """This function compute the fast marching matching methode. 
        take P_tild (can be compute with the functio P_tild) and the coordinate of the initial point"""
    #initilisation
    max_y, max_x = P_tilds.shape
    Us = np.empty_like(P_tilds)
    Us = np.inf
    Us[init_point_y, init_point_x] = 0

    labels = np.empty_like(P_tilds) #FAR=0, TRIAL=1 and ALIVE = 2 
    FAR = 0
    TRIAL = 1
    ALIVE = 2
    labels = FAR 
    labels[init_point_y, init_point_x] = TRIAL

    heaps = [(init_point_y, init_point_x)] #list of trial points


    min_value = np.inf
    min_pix = (0,0)
    while len(heaps) != 0:
        for (point_y,point_x) in heaps:
            if Us[point_y,point_x] < min_value:
                min_value = Us[point_y, point_x] 
                min_pix =(point_y, point_x)
        labels[min_pix[0], min_pix[1]] = ALIVE

        neighbours = pix_neighbours(min_pix[1], min_pix[0], max_x, max_y)

        for neighbour_y, neighbour_x in neighbours:
            if labels[neighbour_y,neighbour_x] != ALIVE:
                current_U = solve_eikonal(Us, min_pix[0], min_pix[1], P_tilds)

                if current_U < Us[min_pix[0],min_pix[1]]:
                    Us[min_pix[0],min_pix[1]] = current_U
                    if labels[neighbour_y,neighbour_x] == FAR:
                        heaps.append((neighbour_y,neighbour_x))
                        labels[neighbour_y,neighbour_x] = TRIAL
                    elif labels[neighbour_y,neighbour_x] == TRIAL:


                


        





