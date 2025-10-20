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
# resize = func.open_image("../Images_TP/Resize.png", "RGB")
# resized = resize.copy()
# for i in range(100):
#     resized = func.seam_carving(resized)
#     print(f'seamcarving aplied {i}')
# plt.subplot(1,2,1)
# plt.imshow(resize)
# plt.subplot(1,2,2)
# plt.imshow(resized)
# plt.show()

#QUESTION4
# img = func.open_image("../Images_TP/Profondeur.png")
# result = func.focus_two_zones(img,
#                          zone1_center=0.70, zone1_width=0.50, z1_top=0.0, z1_bottom=1,
#                          zone2_center=0.40, zone2_width=0.15, z2_top=0.3, z2_bottom=1)

# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title("Image originale")
# plt.imshow(img)
# plt.axis('off')

# plt.subplot(1,2,2)
# plt.title("Effet de profondeur de champ")
# plt.imshow(result)
# plt.axis('off')
# plt.show()

#QUESTION5
# eiffel = func.open_image("../Images_TP/tour-eiffel.jpg", "RGB")
# mask = func.focus_center(eiffel,210, 30)
# plt.subplot(1,2,1)
# plt.imshow(eiffel)
# plt.subplot(1,2,2)
# plt.imshow(mask)
# plt.show()