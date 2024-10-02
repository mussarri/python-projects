import cv2
import cv2.data

try:
    face_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

    img = cv2.imread("IMG_0479.JPG")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for x,y,w,h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    

    cv2.namedWindow("Resize", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Resize", 500, 700) 

    cv2.imshow("Resize", img)
    cv2.waitKey()

    cv2.imwrite("face_detected.jpg", img)
except Exception as e:
    print(e)