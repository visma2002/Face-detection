from deepface import DeepFace
import cv2
trained=cv2.CascadeClassifier("C:\\Users\\91936\\OneDrive\\Desktop\\test\\face.xml")
vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()
    if ret ==True:
     image=cv2.imshow("frame",frame)
     faces=trained.detectMultiScale(frame)
     for x,y,w,h in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
     cv2.imshow("frame",frame)
     cv2.waitKey(1)
    else:
         break

vid.release()
cv2.destroyAllWindows()
