#Indra Kurniawan
#1217070033

import cv2
import numpy as np
import matplotlib.pyplot as plt


gambar = cv2.imread("bean.jpeg")
tinggi_gambar = gambar.shape[0]
lebar_gambar = gambar.shape [1]
channel_gambar = gambar.shape [2]
tipe_gambar = gambar.dtype

brightness_gambar = np.zeros(gambar.shape, dtype=np.uint8)
def brighter (nilai):
  for y in range(0, tinggi_gambar):
    for x in range (0, lebar_gambar):
      red = gambar[y][x][0]
      green = gambar [y][x][1]
      blue = gambar [y][x][2]
      gray = (int(red) + int (green) + int (blue)) /3
      gray+= nilai

      if gray > 255:
        gray = 255
      if gray < 0:
        gray = 0

      brightness_gambar [y][x] = (gray, gray, gray)

brighter(0)
plt.imshow (brightness_gambar)
plt.title("Brightness 0")
plt.show()

brighter(100)
plt.imshow (brightness_gambar)
plt.title("Brightness 100")
plt.show()