import func
import matplotlib.pyplot as plt

def run_q3(): 
    print("3. Mesures \n")
    print("This exercise was quite hard. I had some trouble understanding the documentation.")
    print("\n \n")
    image_piece = func.open_image("../Images_TP/piece.tif", "L")
    func.object_measure(image_piece)
    plt.title("Image to measure")
    plt.imshow(image_piece, cmap="gray")
    plt.show()
