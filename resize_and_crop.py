# -*- coding: utf-8 -*-
"""
Resimlerin Yeniden boyutlandırılması ve kırpılması

Görüntü işlemede resimlerin boyutunu bilip buna göre değiştirmek önemlidir

resim bir arraydir


"""

import cv2
img = cv2.imread(r"C:\Users\Turkuaz\Desktop\goruntu_islem_calisma\Images\logo.png")
print("Resim boyut: ",img.shape)
cv2.imshow("Oriijinal", img)
cv2.waitKey(0)
#Resized yeniden boyutlandırma
img_resized=cv2.resize(img, (800,800))
print("Resized img shape: " ,img_resized.shape)
cv2.imshow("img resized", img_resized)
cv2.waitKey(0)


#kırp
imgCropped=img[:200,0:300]#0 dan 200 e kadar gidiyoruz x ekseninde 0 0 dan başlıyoruz 300 e kadar gidiyoruz y eksenide
#opencv de ilk önce yükseklik sonra genişlik heigt 200 width 300  0 ile 200 arasını al 0 ile 300 arasını al dedik 
cv2.imshow("Cropped img",imgCropped)
cv2.waitKey(0)