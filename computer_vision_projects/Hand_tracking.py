import cv2
import time
import mediapipe as mp

cap=cv2.VideoCapture(0)

mpHand=mp.solutions.hands
hands=mpHand.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

parmak_ids=[
  (8,5),   # işaret parmağı: uç, alt eklem
  (12,9),  # orta parmak
  (16,13), # yüzük parmak
  (20,17)  # serçe parmak
]

while True:
    succes,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        toplam_eller = 0  # tüm ellerin toplam parmak sayısı

        for hand_index, handlms in enumerate(results.multi_hand_landmarks):
            mpDraw.draw_landmarks(img,handlms,mpHand.HAND_CONNECTIONS)

            # Hangi el? ("Left" veya "Right")
            hand_label = results.multi_handedness[hand_index].classification[0].label

            # Landmarkları index'e göre listele
            liste = [None]*21
            for id,lm in enumerate(handlms.landmark):
                h,w, c = img.shape
                cx,cy=int (lm.x*w),int(lm.y*h)
                liste[id] = [cx,cy]

                # id==0 için daire
                if id==0:
                    cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)

            # Parmak sayma
            parmaklar=[]
            for uc,alt in parmak_ids:
                if liste[uc][1]<liste[alt][1]:  # y koordinatına göre işaret parmağı vs
                    parmaklar.append(1)
                else:
                    parmaklar.append(0)

            # Baş parmak (x koordinatına göre)
            if hand_label == "Right":
                parmaklar.append(1 if liste[4][0] > liste[3][0] else 0)
            else:
                parmaklar.append(1 if liste[4][0] < liste[3][0] else 0)

            toplam_eller += sum(parmaklar)

        # Tek text olarak göster
        cv2.putText(img, str(toplam_eller), (10, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    # FPS hesaplama
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,"FPS: "+str(int(fps)),(10,75),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),5)

    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break