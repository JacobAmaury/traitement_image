import func
import matplotlib.pyplot as plt

image_path = ["../images/1.png", "../images/2.png", "../images/3.png"]

image = func.open_image("../images/1.png", "L")
image_pretraited = func.pretreatment(image)
P_tilde_mode0 = func.p_tild(image_pretraited, 0, alpha=80, sigma=1.5, omega=0.1)
P_tilde_mode1 = func.p_tild(image_pretraited, 1,alpha=80, sigma=1.5, omega=0.1)


plt.subplot(2,3,1)
plt.title("base image")
plt.imshow(image, cmap="gray")

plt.subplot(2,3,2)
plt.title("image pretraited")
plt.imshow(image_pretraited*255, cmap="gray")

plt.subplot(2,3,3)
plt.title("P_tilde mode 0")
plt.imshow(P_tilde_mode0*255, cmap="gray")

plt.subplot(2,3,4)
plt.title("P_tilde mode 1")
plt.imshow(P_tilde_mode1*255, cmap="gray")
plt.show()