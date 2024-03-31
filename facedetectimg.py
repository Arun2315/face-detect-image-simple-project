import cv2

alg = "haarcascade_frontalface_default.xml" #inilize the paste od local d disk

haar_cascade = cv2.CascadeClassifier(alg) #syntax for the any staring program and load algorithm

video_path="ajithkumar.jpeg"
img = cv2.imread(video_path)
##cam=cv2.VideoCapture(video_path) #camera id number

while True:
##    ret,img = cam.read() #reading the frame of the image

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convret gray color image this is rule mandornty

    face = haar_cascade.detectMultiScale(gray_img,1.3,4) #alg passing to multiple face dectect panum 1.3 is resize 4 means 4 face pakum

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #xy 
    cv2.imshow("FaceDetection",img) #display

    key =cv2.waitKey(1) #10per second wait pannum
    ##print(key)  this pana -1 varum avolotha
    print(key)
    if key ==27: 
        break
img.release()
cv2.destroyAllWindows()

