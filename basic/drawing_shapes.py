import cv2
import numpy as np

# numpy kütüphanesi ile görüntü oluşturucaz

img=np.zeros((512,512,3),np.uint8)#np.zeros sıfırlardan oluşur 512x512 boyutta 3 boyutlarına sahip 0lar int olacak
#siyah 0 yaklaştıkca görünür pikselin genliği
print(img.shape)

#Görüntüyü görselleştirdik
cv2.imshow("Siyah",img)
cv2.waitKey(0)
#line(cizgi) oluştur 
cv2.line(img, (0,0), (512,512), (0,255,0),3)# 0,0 başlangıc nokası 512,512 bitiş noktası ,renk,kalınlık

cv2.line(img,(100,100),(100,300),(0,100,0),3)

cv2.imshow("line", img)
cv2.waitKey(0)

#Dikdörtgen
#(resim,başlangıc bitiş)
cv2.rectangle(img, (100,100),(256,256),(255,0,0),cv2.FILLED)#cvfilled dikdörtgenin içini doldurur
cv2.imshow("Dikdortgen",img)
cv2.waitKey(0)

#çember
#(resim,merkez,yarı çap,renk)
cv2.circle(img, (300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("Dikdortgen",img)
cv2.waitKey(0)

#metin
#(resim,başlangıc noktası,font,kalınlık,renk)
cv2.putText(img, "Furkan", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255))
cv2.imshow("Metin",img)
cv2.waitKey(0)
