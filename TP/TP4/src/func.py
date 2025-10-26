import numpy as np
from PIL import Image
import time
from scipy.ndimage import binary_erosion
from scipy.ndimage import binary_dilation
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops


def open_image(path, mode="RGB"):
    img = np.array(Image.open(path).convert(mode), int)
    return img

def photomaton(image):
    h,w,_ = image.shape
    new_image =  np.zeros_like(image)
    half_im_x = w//2
    half_im_y = h//2
    for y in range(0,h,2):
        for x in range(0,w,2):
            new_image[y//2,x//2] = image[y,x]
            new_image[y//2,(x//2+half_im_x)] = image[y,x+1]
            new_image[(y//2+half_im_y),x//2] = image[y+1,x]
            new_image[y//2+half_im_y,x//2+half_im_y] = image[y+1,x+1]

    return(new_image)


import random as rd

def all_RGB(image):
    t1 = time.time()
    
    h,w,_ = image.shape
    image_2 = np.empty_like(image)
    used_pixel = set() #like a list but only with unique element 
    max_rand = 6
    

    for y in range(h):
        for x in range(w):
            R,G,B = image[y,x]
            triplet = (int(R), int(G), int(B))

            while triplet in used_pixel:      

                outR = triplet[0]+rd.randint(-max_rand,max_rand)
                if outR>255: outR = 255
                if outR<0: outR = 0
                outG = triplet[1]+rd.randint(-max_rand,max_rand)
                if outG>255: outG = 255
                if outG<0: outG = 0
                outB = triplet[2]+rd.randint(-max_rand,max_rand)
                if outB>255: outB = 255
                if outB<0: outB = 0

                triplet = (outR, outG, outB)
            image_2[y, x] = triplet
            used_pixel.add(triplet)
    
    t2 = time.time()
    print(f"temps de calcule: {t2-t1}s")
    return image_2.astype(int)





def object_measure(image):
    struct = np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]])
    threshold = threshold_otsu(image)
    binary = image > threshold
    binary = binary_dilation(binary, structure=struct, iterations=2)
    binary = binary_erosion(binary, structure=struct, iterations=2)
    binary_2 = binary[20:-20,20:-20] #avoid edge 

    labeled_piece = label(~binary_2) 
    props_piece = regionprops(labeled_piece)

    labeled_holes = label(binary_2)
    props_holes = regionprops(labeled_holes)
    
    cpt = 0
    for i in range(1, len(props_holes)):
        minr, minc, maxr, maxc = props_holes[i].bbox
        largeur = maxc - minc
        hauteur = maxr - minr
        aire = props_holes[i].area
        print(f"circle {cpt}: width={largeur}, height={hauteur}, surface={aire}")
        cpt += 1

    cpt = 0
    for i in range(0, len(props_piece)):
        minr, minc, maxr, maxc = props_piece[i].bbox
        largeur = maxc - minc
        hauteur = maxr - minr
        aire = props_piece[i].area
        print(f"object {cpt}: width={largeur}, height={hauteur}, surface={aire}")
        cpt += 1

    return binary_2.astype(int)


