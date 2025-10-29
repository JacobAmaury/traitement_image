import func
import matplotlib.pyplot as plt


start_x = 218
start_y = 328

end_x = 171
end_y = 97

image_path = ["../images/1.png", "../images/2.png", "../images/3.png"]

image = func.open_image("../images/1.png", "L")
image_pretraited = func.pretreatment(image)
P_tilde_mode0 = func.p_tild(image_pretraited, 0, alpha=80, omega=0.1)
P_tilde_mode1 = func.p_tild(image_pretraited, 1,alpha=80, omega=0.1)


Us = func.fast_marching(P_tilde_mode0, start_x, start_y)
paths = func.backtrack(Us, start_x, start_y, end_x, end_y, 0.5, 5000)


plt.subplot(2,3,1)
plt.title("base image")
plt.imshow(image, cmap="gray")

plt.subplot(2,3,2)
plt.title("image pretraited")
plt.imshow(image_pretraited*255, cmap="gray")
plt.plot(paths)

plt.show()