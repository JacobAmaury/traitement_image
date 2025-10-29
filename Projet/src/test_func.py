import func
import matplotlib.pyplot as plt
import numpy as np

start_x = [26,56,3]
start_y = [65,206,66]

end_x = [355,134,338]
end_y = [155,70,221]
image_nb = 2


image_path = ["../images/1.png", "../images/2.jpg", "../images/3.png"]



print("1")
image = func.open_image(image_path[image_nb], "L")
image_pretraited = func.pretreatment(image)

print("2")
P_tilde = func.p_tild(image_pretraited, mode=1, alpha=50, sigma=0.02, omega=0.01)

print("3")

Us = func.fast_marching(P_tilde, start_x[image_nb], start_y[image_nb])
print("4")
paths = func.backtrack(Us, start_x[image_nb], start_y[image_nb], end_x[image_nb], end_y[image_nb], 0.5, 5000)

print("5")
paths = np.array(paths)

plt.subplot(2,3,1)
plt.title("base image")
plt.imshow(image, cmap="gray")
plt.plot(paths[:,0], paths[:,1], 'cyan', lw=2)

plt.scatter([start_x[image_nb], end_x[image_nb]], [start_y[image_nb], end_y[image_nb]], c='red', marker='o')

plt.subplot(2,3,2)
plt.title("image pretraited")
plt.imshow(image_pretraited*255, cmap="gray")
plt.plot(paths[:,0], paths[:,1], 'cyan', lw=2)

plt.scatter([start_x[image_nb], end_x[image_nb]], [start_y[image_nb], end_y[image_nb]], c='red', marker='o')

plt.subplot(2,3,3)
plt.imshow(P_tilde, cmap='jet')
plt.title("Carte de coût (P)")
plt.colorbar()

plt.subplot(2,3,4)
plt.imshow(Us, cmap='jet')
plt.title("Carte de U")
plt.colorbar()
plt.plot(paths[:,0], paths[:,1], 'cyan', lw=2)

plt.scatter([start_x[image_nb], end_x[image_nb]], [start_y[image_nb], end_y[image_nb]], c='red', marker='o')

plt.show()
