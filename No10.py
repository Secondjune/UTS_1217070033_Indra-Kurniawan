#Indra Kurniawan
#1217070033

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('bean.jpeg')

b, g, r = cv2.split(image)

hist_b = cv2.calcHist([b], [0], None, [256], [0,256])
hist_g = cv2.calcHist([g], [0], None, [256], [0,256])
hist_r = cv2.calcHist([r], [0], None, [256], [0,256])

plt.figure(figsize=(10, 6))
plt.plot(hist_r, color='r', label='R')
plt.plot(hist_g, color='g', label='G')
plt.plot(hist_b, color='b', label='B')
plt.title('rgb histogram')
plt.xlabel('intensitas')
plt.ylabel('frequensi')
plt.legend()
plt.grid()
plt.show()