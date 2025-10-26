
import func
import matplotlib.pyplot as plt

def run_q3(): 
    print("1. Le photomaton")
    image_piece = func.open_image("../Images_TP/piece.tif", "L")
    func.object_measure(image_piece)

run_q3()