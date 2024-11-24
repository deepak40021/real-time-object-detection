import cv2
facedata= cv2.CascadeClassifier("C:/Users/DEEPAK KUMAR/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/datahaarcascade_frontalface_default.xml")
vid=cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,460)
while True:
    success,img=vid.read()
    col=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedata.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in  faces:
        cv2.rectangle(img,(x,y),(x+w),(0,255,0),2)
    cv2.imshow('webcam',img)
    key = cv2.waitKey(1)
    if  key ==  ord ('r'):
        break
vid.release()
cv2.destroyAllWindows() 


#vid=cv2.VideoCapture(0)
#vid.set(3,640)
#vid.set(4,460)
#while True:
 #   success,img=vid.read()
  #  cv2.imshow('webcam',img)
   # key = cv2.waitKey(1)
    #if  key ==  ord ('r'):
     #   break
#vid.release()