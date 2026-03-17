import cv2
import time

#Video okuma,video boyutunu ayarlamyı ve video gösterme
#Video resimlerin ard arda oynamasıdır


#video ismi

video_name="WIN_20260313_03_42_19_Pro.mp4"
#video iççe aktar:capture,cap
cap=cv2.VideoCapture(video_name)#videoyu degiskene atadık

print("Genislik: ",cap.get(3))
print("Yükseklik:",cap.get(4))

#Videocapture yaptıgımız zaman video boş olsa bile yükler ama doğru bir şekilde acıp acmadıgımızı kontrol etmemiz lazım

if cap.isOpened()==False:
    print("Hata")
    
#read metodu ret(return) ve frame(videoda ki her bir resim) döndürür 
#Return ise cap read başarılı olduysa true yanlış olduysa false döndürecek


while True:# while dongusune almasaydık cok hızlı bir şekilde açılıp kapanırdı pencere
    ret,frame=cap.read()#Çünkü resim gösteriyor aslında o yüzde yavaşlatıp bakıyoruz while da
    if ret==True:
     
        time.sleep(0.1)
        cv2.imshow("Video",frame)
    else:break
    
    if cv2.waitKey(1)&0xFF==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
        
