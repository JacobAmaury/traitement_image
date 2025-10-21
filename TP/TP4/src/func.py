import numpy as np
from PIL import Image


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

# def all_RGB(image):
#     h,w,_ = image.shape
#     new_im = np.empty_like(image)
#     max_value_RGB = 255
#     triplets = []
#     for y in range(h):
#         for x in range(w):
#             act_triplet = image[y,x]
#             cpt_R = 0
#             cpt_G = 0
#             cpt_B = 0
#             is_equal = False
#             while is_equal == False:
                  
    
#     return(new_im)



def threshold(image, seuil):
    image[image>seuil] = 1
    image[image<=seuil] = 0
    return image

def dilatation(image):
    structural_element = np.array([[0,1,0],
                                   [1,1,1],
                                   [0,1,0]])
    struct_h = structural_element.shape[0] // 2
    sum_structu = np.sum(structural_element)
    new_image = np.empty_like(image)
    h,w = image.shape
    for y in range(h):
        for x in range(w):
            if (x>struct_h and x-struct_h<w) and (y>struct_h and y-struct_h<h):
                if(np.sum(image[x-struct_h:x+struct_h, y-struct_h:y+struct_h]*structural_element)) >= 1:
                    new_image[x,y] = 1
    return new_image 
    