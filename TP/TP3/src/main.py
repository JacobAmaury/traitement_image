#*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 14102025 15:49:36     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

#QUESTION1
path_images = ["../Images_TP/Refocus_1.png", "../Images_TP/Refocus_2.png", "../Images_TP/Refocus_3.png"]
refocus = func.refocus(path_images)
plt.imshow(refocus)
plt.show()

#QUESTION2
# mosaic_1 = "../Images_TP/Mosaic_1.png"
# mosaic_2 = "../Images_TP/Mosaic_2.png"
# func.mosaic(mosaic_1, mosaic_2)

#QUESTION3

resize = func.open_image("../Images_TP/Resize.png", "RGB")
energy = func.energy_map_sobel(resize)
plt.imshow(energy, cmap='gray')
plt.show()