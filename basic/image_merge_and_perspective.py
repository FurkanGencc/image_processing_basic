#Görüntülerin birleştirilmesi

import cv2
import numpy as np
img=cv2.imread("logo.png")
cv2.imshow("Resim",img)
cv2.waitKey(0)

#yatay birleştirme
hor=np.hstack((img,img))# img aslında array iki arrayi numpy da birleştiriyoruz
cv2.imshow("Horizontal", hor)
cv2.waitKey(0)
#dikey
ver=np.vstack((img,img))
cv2.imshow("Veritcal", ver)
cv2.waitKey(0)

#Perspektif çarpıtma

img2=cv2.imread("logo_dondurulmus.png")
cv2.imshow("Resim",img2)
print(img2.shape)
cv2.waitKey(0)
points1=np.float32([[52,721],[397,381],[769,744],[415,1115]])#dondurulmus görselin 4 adet konumu
points2=np.float32([[541,50],[900,395],[542,760],[178,350]])#buda ana konum

matris=cv2.getPerspectiveTransform(points1, points2)#perspektif transform matirisini elde ettik
print(matris)
imgOutput=cv2.warpPerspective(img2, matris, (1280,800))#cevirme işlemini gerçekleştirdik
cv2.imshow("Resim",imgOutput)
cv2.waitKey(0)
