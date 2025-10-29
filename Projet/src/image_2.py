import func
import time
import numpy as np
import matplotlib.pyplot as plt

def run_image_2():
    print("This image was find on iternet (all the sources are in the images folder).\nThe parameters of p_tild are: mode=1, sigma=0.02, omega=0.1")
    print("The computation time is approximately 3s")
    # Initialisation
    start_x = 56
    start_y = 206
    end_x = 134
    end_y = 70
    image_path = "../images/2.jpg"

    t1 = time.time()
    image = func.open_image(image_path, "L")
    image_pretreated = func.pretreatment(image)
    t2 = time.time()
    print(f"Preprocessing done in: {t2 - t1:.3f}s")
    P_tilde = func.p_tild(image_pretreated, mode=1, alpha=50, sigma=0.02, omega=0.1)
    t3 = time.time()
    print(f"Computation of P_tilde done in: {t3 - t2:.3f}s")

    Us = func.fast_marching(P_tilde, start_x, start_y)
    t4 = time.time()
    print(f"Computation of Us done in: {t4 - t3:.3f}s")

    paths = func.backtrack(Us, start_x, start_y, end_x, end_y, 0.5, 5000)
    t5 = time.time()
    print(f"Computation of the path done in: {t5 - t4:.1f}s")
    print(f"Total computation time: {t5 - t1:.3f}s")

    paths = np.array(paths)

    # Plot
    plt.figure(figsize=(10, 7))

    plt.subplot(2, 3, 1)
    plt.title("Base image")
    plt.imshow(image, cmap="gray")

    plt.subplot(2, 3, 2)
    plt.title("Preprocessed image")
    plt.imshow(image_pretreated * 255, cmap="gray")

    plt.subplot(2, 3, 3)
    plt.imshow(P_tilde, cmap='jet')
    plt.title("P_tilde map")

    plt.subplot(2, 3, 4)
    plt.imshow(Us, cmap='jet')
    plt.title("Distance map (U)")

    plt.subplot(2, 3, 5)
    plt.title("Base image with path")
    plt.imshow(image, cmap="gray")
    plt.plot(paths[:, 0], paths[:, 1], 'cyan', lw=2)
    plt.scatter([start_x, end_x], [start_y, end_y], c='red', marker='o')

    plt.tight_layout()
    plt.show()
