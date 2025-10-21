
import func
import matplotlib.pyplot as plt

def run_q3(): 
    print("1. Le photomaton")
    image_piece = func.open_image("../Images_TP/piece.tif", "L")
    image_test = func.threshold(image_piece, 155)
    # image_test = func.dilatation(image_test)
    image_test *= 255   
    
    plt.imshow(image_test)
    plt.show()

