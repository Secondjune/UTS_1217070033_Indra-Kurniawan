# Indra Kurniawan
# 1217070033

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title='image', cmap_type='gray'):
    plt.figure()
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def calculate_normalized_histogram(image):
    histogram, _ = np.histogram(image, bins=256, range=(0, 256))

    total_pixels = image.size

    normalized_histogram = histogram / total_pixels

    return normalized_histogram

def calculate_cumulative_histogram(normalized_histogram):
    cumulative_histogram = np.cumsum(normalized_histogram)
    return cumulative_histogram

image_path = 'bean.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

show_image(image, title='Normalisasi Citra')

normalized_histogram = calculate_normalized_histogram(image)
cumulative_histogram = calculate_cumulative_histogram(normalized_histogram)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(range(256), normalized_histogram, color='black')
plt.title('Normalisasi Histogram Citra')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Distribusi Probabilitas')

plt.subplot(1, 2, 2)
plt.plot(cumulative_histogram, color='black')
plt.title('Histogram Kumulatif')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Distribusi Kumulatif')

plt.show()
