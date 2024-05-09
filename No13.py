# Indra Kurniawan
# 1217070033

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("bean.jpeg")

rotated_image = imutils.rotate(image, -90, scale=0.5)

plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.title('Citra Rotasi')
plt.axis('off')
plt.show()
