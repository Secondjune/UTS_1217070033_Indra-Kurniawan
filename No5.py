#Indra Kurniawan
#1217070033

import matplotlib.pyplot as plt
import cv2
original = cv2.imread('bean.jpeg')

red = original[:,:,0]
green = original[:,:,1]
blue = original[:,:,2]

print('Red Shape =',red.shape)
print('Green Shape =',green.shape)
print('Blue Shape =', blue.shape)

fig, axes = plt.subplots(2,2, figsize=(10,10))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title('Citra input')

ax[1].imshow(red,cmap=plt.cm.gray)
ax[1].set_title('Red Channel')

ax[2].imshow(red,cmap=plt.cm.gray)
ax[2].set_title('Green Channel')

ax[3].imshow(red,cmap=plt.cm.gray)
ax[3].set_title('Blue Channel')

fig.tight_layout()
plt.show()