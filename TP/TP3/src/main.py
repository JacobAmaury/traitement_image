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
# path_images = ["../Images_TP/Refocus_1.png", "../Images_TP/Refocus_2.png", "../Images_TP/Refocus_3.png"]
# refocus = func.refocus(path_images)
# plt.imshow(refocus)
# plt.show()

#QUESTION2
# mosaic_1 = "../Images_TP/Mosaic_1.png"
# mosaic_2 = "../Images_TP/Mosaic_2.png"
# func.mosaic(mosaic_1, mosaic_2)

#QUESTION3
#This function is so slow this is a shame
resize = func.open_image("../Images_TP/Resize.png", "RGB")
resized = resize.copy()
for i in range(100):
    resized = func.seam_carving(resized)
    print(f'seamcarving aplied {i}')
plt.subplot(1,2,1)
plt.imshow(resize)
plt.subplot(1,2,2)
plt.imshow(resized)
plt.show()