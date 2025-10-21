import func
import matplotlib.pyplot as plt

def run_q1(): 
    print("1. Le photomaton")
    image_MonaLisa = func.open_image("../Images_TP/MonaLisa_square.jpg")
    new_Mona = func.photomaton(image_MonaLisa)
    for i in range(11):
        new_Mona = func.photomaton(new_Mona)
    
    plt.imshow(new_Mona)
    plt.show()


