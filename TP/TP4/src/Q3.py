
import func
import matplotlib.pyplot as plt

def run_q3(): 
    print("1. Le photomaton")
    image_piece = func.open_image("../Images_TP/piece.tif", "L")
    image_test = func.object_measure(image_piece)
    # image_test = func.dilatation(image_test)
    image_test *= 255   
    
    plt.imshow(image_test, cmap="grey")
    plt.show()

run_q3()