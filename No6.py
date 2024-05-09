# Indra kurniawan
# 1217070033

import matplotlib.pyplot as plt
import cv2
original = cv2.imread('bean.jpeg')

red = original.copy()#red channel(0)
red[:,:,1]=0
red[:,:,2]=0
print('Red Shape =',red.shape)

green = original.copy()#green channel(0)
green[:,:,0]=0
green[:,:,2]=0
print('Green Shape =',green.shape)

blue = original.copy()#blue channel(0)
blue[:,:,0]=0
blue[:,:,1]=0
print('Blue Shape =',blue.shape)

fig,axes= plt.subplots(2,2, figsize=(10,10))
ax = axes.ravel()
ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(red)
ax[1].set_title("Red Channel")
ax[2].imshow(green)
ax[2].set_title("Green Channel")
ax[3].imshow(blue)
ax[3].set_title("Blue Channel")
fig.tight_layout()
plt.show()


