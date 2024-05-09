#Indra Kurniawan
#1217070033

import cv2


gambar = cv2.imread('bean.jpeg')

tinggi, lebar = gambar.shape[:2]

ukuran_data = gambar.size

tipe_data = gambar.dtype

print(f"Resolusi gambar: {tinggi}x{lebar}")
print(f"Ukuran data: {ukuran_data} bytes")
print(f"Tipe data: {tipe_data}")
