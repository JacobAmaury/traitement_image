import func
import matplotlib.pyplot as plt

def run_q1(): 
    print("1. Le photomaton \n")
    i = int(input("Enter the number of iterations. If you select 12, you will return to the base image: "))-1
    print("This exercise was quite interesting. The fact that we don't lose information is impressive.")
    image_MonaLisa = func.open_image("../Images_TP/MonaLisa_square.jpg")
    new_Mona = func.photomaton(image_MonaLisa)
    for i in range(i):
        new_Mona = func.photomaton(new_Mona)
    
    plt.imshow(new_Mona)
    plt.show()


