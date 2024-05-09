# Indra Kurniawan
# 1217070033

import cv2

image = cv2.imread('bean.jpeg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue = hsv[:,:,0]
saturation = hsv[:,:,1]
value = hsv[:,:,2]

cv2.imshow('Hue', hue)
cv2.imshow('Saturation', saturation)
cv2.imshow('Value', value)

cv2.waitKey(0)

cv2.destroyAllWindows()
