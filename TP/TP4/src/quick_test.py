import func
import matplotlib.pyplot as plt

image_Lena = func.open_image("../Images_TP/Lena.jpg")
image = func.all_RGB(image_Lena)
plt.imshow(image)
plt.show()

