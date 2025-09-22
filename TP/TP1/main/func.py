import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import func as fn
import PIL
from PIL import Image


def convert_to_red(image):
    new_im = Image.new(mode="RGBA", size=image.size)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            R, G, B, A = image.getpixel((i, j))
            new_im.putpixel((i, j), (R, 0, 0, A))
    return new_im
