#Indra Kurniawan
#1217070033

import cv2
img = cv2.imread('bean.jpeg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()