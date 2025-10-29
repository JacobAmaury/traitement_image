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
    image = cv.GaussianBlur(image,(5,5),0)
    return image

def p_tild(image, mode=0, alpha=50, sigma=1.0, omega=0.05):
    """Compute p_tild.
       if mode=0: P = exp(-alpha*g^2)
       else: P = 1 / (1 + (g/sigma)^2)
    """
    Gy, Gx = np.gradient(image)
    g = np.sqrt(Gx**2 + Gy**2)

    if mode == 0:
        P = np.exp(-alpha * (g ** 2))
    else:
        P = 1 / (1 + (g / sigma) ** 2)
    P_tild = omega + P
    return P_tild


def is_pix(x, y, max_x, max_y):
    """return 1 when the x or y are not on the side"""
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
    h,w = Us.shape
    p_tild = P_tilds[pix_y,pix_x]

    if is_pix(pix_x-1, pix_y, w, h) and is_pix(pix_x+1, pix_y, w, h):
        a = min(Us[pix_y, pix_x-1],Us[pix_y, pix_x+1])
    else:
        if is_pix(pix_x-1, pix_y, w, h):
            a = Us[pix_y, pix_x-1]
        else :
            a = Us[pix_y, pix_x+1]

    if is_pix(pix_x, pix_y-1, w, h) and is_pix(pix_x, pix_y+1, w, h):
        b = min(Us[pix_y-1, pix_x],Us[pix_y+1, pix_x])
    else:
        if is_pix(pix_x, pix_y-1, w, h):
            b = Us[pix_y-1, pix_x]
        else :
            b = Us[pix_y+1, pix_x]

    if abs(a - b) >= p_tild:
        U_new = min(a, b) + p_tild
    else:
        U_new = (a + b + np.sqrt(2 * p_tild ** 2 - (a - b) ** 2)) / 2.0
    return U_new


def fast_marching(P_tilds, init_point_x, init_point_y):
    max_y, max_x = P_tilds.shape
    Us = np.full_like(P_tilds, np.inf)
    Us[init_point_y, init_point_x] = 0.0

    FAR = 0
    TRIAL = 1
    ALIVE = 2

    labels = np.full_like(P_tilds, FAR, dtype=int)
    labels[init_point_y, init_point_x] = TRIAL

    heaps = [(init_point_y, init_point_x)]

    while len(heaps) != 0:
        # Trouve le pixel de U minimal
        min_val = np.inf
        min_pix = None
        for (point_y, point_x) in heaps:
            if Us[point_y, point_x] < min_val:
                min_val = Us[point_y, point_x]
                min_pix = (point_y, point_x)
        
        if min_pix is None: break

        heaps.remove(min_pix)
        labels[min_pix] = ALIVE

        for ny, nx in pix_neighbours(min_pix[1], min_pix[0], max_x, max_y):
            if labels[ny, nx] != ALIVE:
                U_new = solve_eikonal(Us, ny, nx, P_tilds)
                if U_new < Us[ny, nx]:
                    Us[ny, nx] = U_new
                    if labels[ny, nx] == FAR:
                        heaps.append((ny, nx))
                        labels[ny, nx] = TRIAL

    return Us





def backtrack(Us, start_x, start_y, end_x, end_y, step, max_it):
    paths = [(end_x, end_y)]
    current_x = end_x
    current_y = end_y
    avoid_0_div = 1e-6
    cpt = 0
    while not((current_x == start_x) and (current_y == start_y)) and (cpt < max_it):
        dUx = Us[int(current_y), int(current_x+1)] - Us[int(current_y), int(current_x)]
        dUy = Us[int(current_y+1), int(current_x)] - Us[int(current_y), int(current_x)]

        norm_grad = np.sqrt(dUx**2+dUy**2+avoid_0_div)
        normalized_dUx = dUx/norm_grad
        normalized_dUy = dUy/norm_grad

        current_x -= step * normalized_dUx
        current_y -= step * normalized_dUy

        paths.append((int(current_x), int(current_y)))
        cpt += 1
    return paths

