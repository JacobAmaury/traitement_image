import func
import matplotlib.pyplot as plt

def run_q2(): 
    print("2. All RGB \n")
    print("I have tried many variations of this code and explored many approaches. This method is the quickest I found.")
    print("The results are okay. I think that if I had more time, I could optimize the function.")
    print("On the all RGB image we can see some noise")
    image_Lena = func.open_image("../Images_TP/Lena.jpg")
    image = func.all_RGB(image_Lena)

    plt.subplot(1,2,1)
    plt.imshow(image_Lena)
    plt.title("Base image")
    plt.subplot(1,2,2)
    plt.title("All RGB image")
    plt.imshow(image)
    plt.show()



