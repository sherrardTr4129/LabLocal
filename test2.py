#opens up a webcam feed so you can then test your classifer in real time
#using detectMultiScale
import numpy
import cv2

def detect(img):
    hammer = cv2.CascadeClassifier("hammer.xml")
    drill = cv2.CascadeClassifier("handDrill.xml")
    saw = cv2.CascadeClassifier("saw.xml")
    wireCutter = cv2.CascadeClassifier("WireCutter.xml")
    hammerRects = hammer.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (335,335))
    sawRects = saw.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (300,300))
    drillRects = drill.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (300,300))
    wireRects = wireCutter.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (300,300))

    if (len(hammerRects) == 0 and len(sawRects) == 0 and len(drillRects) == 0 and len(wireRects) == 0):
        return [], img, ""
    elif(len(hammerRects) != 0):
        hammerRects[:, 2:] += hammerRects[:, :2]
        return hammerRects, img, "hammer"
    elif(len(sawRects) != 0):
        sawRects[:, 2:] += sawRects[:, :2]
        return sawRects, img, "hand saw"
    elif(len(drillRects) != 0):
        drillRects[:, 2:] += drillRects[:, :2]
        return drillRects, img, "hand drill"
    elif(len(wireRects) != 0):
	wireRects[:, 2:] += wireRects[:, :2]
	return wireRects, img, "wire cutter"

def box(rects, img, txt):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
	cv2.putText(img,txt,(x1,y1),  cv2.FONT_HERSHEY_SIMPLEX, .75,(255,0,0),2,10)


cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    rects, img, detected = detect(img)
    box(rects, img, detected)
    cv2.imshow("frame", img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
	break
