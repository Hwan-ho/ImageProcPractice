from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = np.array(Image.open('/public/pythonPractice/lena_gray.jpeg'))

bitdepth = 3
image_bitdepth = image//(256//2**bitdepth)

plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray', interpolation='none')
plt.title('bit-depth: 8')
plt.subplot(1,2,2)
plt.imshow(image_bitdepth, cmap='gray', interpolation='none')
plt.title(f'bit-depth: {bitdepth}')
