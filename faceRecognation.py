import cv2

cascade = cv2.CascadeClassifier("C:/Users/Harsh/AppData/Roaming/Python/Python311/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#Here in cascadeclassifier put location of " haarcascade_frontalface_default.xml " from your download location in opencv package file
capture = cv2.VideoCapture(0)

while True:
    rat , video_data = capture.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        #this will convert video into gray for face detection


    face = cascade.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for(x,y,w,h) in face:
        cv2.rectangle(video_data,(x,h),(x+w,y+h),(0,255,0),2)

    frame = cv2.flip(video_data,1)
    
    cv2.imshow("video_live", frame)
    if cv2.waitKey(10) == ord("a") :
        break
#press "a" to stop camara from recognizing 
capture.release() 
