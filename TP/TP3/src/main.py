#*
#* Auteur : Jacob Amaury                 |\      _,,,---,,_
#* Date   : 14102025 15:49:36     ZZZzz  /,`.-'`'    -.  ;-;;,_
#*                                      |,4-  ) )-,_. ,\ (  `'-' 
#*/                                    '---''(_/--'  `-'\_)

import func
import matplotlib.pyplot as plt
import numpy as np
import cv2

<<<<<<< HEAD
#QUESTION1
# path_images = ["../Images_TP/Refocus_1.png", "../Images_TP/Refocus_2.png", "../Images_TP/Refocus_3.png"]
# refocus = func.refocus(path_images)
# plt.imshow(refocus)
# plt.show()
=======
import os 
import sys
import time
import q1
import q3
import q4
import q5



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress enter to get back to the menu")

def menu():
    while True:
        clear_screen()
        print("===============================")
        print("TP3")
        print("Question 6 and 7 are in src/question6 or 7")
        print("===============================")
        print("1. Re-focusing of an image from a sequence.")
        print("3. Context-Aware Image Resizing")
        print("4. Interactive Depth of Field.")
        print("5. Focus on the center of interest of an image without distorting the overall image or context too much.")
        print("6. Quit")
        print("===============================")
        choice = 0
        choice = input("Choose one of the topics: ").strip()
        
        if choice == "1":
            clear_screen()
            q1.run_q1()
            pause()
        elif choice == "3":
            clear_screen()
            q3.run_q3()
            pause()
        elif choice == "4":
            clear_screen()
            q4.run_q4()
            pause()
        elif choice == "5":
            clear_screen()
            q5.run_q5()
            pause()
        elif choice == "6":
            break    


menu()

>>>>>>> 9f9df01dd37dda689863d473166daf9bf7bc2cb4


<<<<<<< HEAD
#QUESTION3
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
=======
>>>>>>> 9f9df01dd37dda689863d473166daf9bf7bc2cb4

