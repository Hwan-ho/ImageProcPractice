import matplotlib.pyplot as plt
import numpy as np

image = np.random.random((10, 10)) * 255

# Display the image
plt.imshow(image, cmap='gray')
plt.colorbar(label='Intensity')

# Annotate each pixel with its intensity value
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        plt.text(j, i, f'{int(image[i, j])}', ha='center', va='center', color='red', fontsize=8)