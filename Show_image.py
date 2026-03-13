import cv2  # opencv

# Resmi içe aktarma
img = cv2.imread("logo.png", 0)  # 0 = grayscale

# Pencereyi büyütülebilir yap
cv2.namedWindow("ilk resim", cv2.WINDOW_NORMAL)

# Görselleştir
cv2.imshow("ilk resim", img)

k=cv2.waitKey(0) &0xFF#klavyeye baglantı yapıyoruz

if k==27:#escape tusu degeri 27 esc
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite("logo_gray.png", img)#Dosyayı s tusu ile kayıt ettim
    cv2.destroyAllWindows()

#Resim iki boyuttan oluşan matrislerdir
#Resim 0-255 arasında genliklerden oluşur
#Bu resim de 800çarpı1280 tane piksel var
#her bir array elemanı piksel