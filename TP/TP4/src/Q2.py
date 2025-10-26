import func
import matplotlib.pyplot as plt

def run_q2(): 
    print("1. Le photomaton")
    image_Lena = func.open_image("../Images_TP/Lena.jpg")
    image = func.all_RGB(image_Lena)
    plt.imshow(image)
    plt.show()



