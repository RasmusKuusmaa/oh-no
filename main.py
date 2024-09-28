import cv2 as cv
import random
video = cv.VideoCapture('crowd.mp4')
substractor = cv.createBackgroundSubtractorMOG2(random.randint(1, 10000), random.randint(1, 100))
i = 0 
while True:
    if i % 20 == 0:
        substractor = cv.createBackgroundSubtractorMOG2(random.randint(1, 10000), random.randint(1, 100))
    i += 1
    ret, frame = video.read()
    if ret:
        mask = substractor.apply(frame)
        cv.imshow('mastk', mask)
        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture('crowd.mp4')
cv.destroyAllWindows()
video.release()