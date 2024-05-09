#Indra Kurniawan
#1217070033

import cv2
img = cv2.imread('bean.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
