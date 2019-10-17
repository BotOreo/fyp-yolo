import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

#nak pakai ni kena tukar self offset dekat loader.py  check elok2
options =\
    {
    'model': 'cfg/yolo.cfg',
    'load' : 'bin/yolov2.weights', #load the weight
    'threshold' : 0.3, #define threshold = how much of a factor it needs to have to draw the bounding box
    'gpu' : 0.75
    }

tfnet =TFNet(options)
capture = cv2.VideoCapture('vidtest5.mp4')
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret,frame = capture.read()
    results = tfnet.return_predict(frame)
    if ret:
        #this is for bounding box------------------------------------------
        for color, result in zip(colors,results):
            tl = (result['topleft']['x'], result['topleft']['y'])  # pixel coordinate
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame = cv2.rectangle(frame, tl, br, color, 2)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #this is for bounding box -----------------------------
        cv2.imshow('frame',frame)
        print('FPS {:.1f}'.format(1/(time.time() - stime)))#Display FPS rate inferencing
        if cv2.waitKey(1) & 0xFF == ord('q'): #Press Q tu exit the inferencing
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break