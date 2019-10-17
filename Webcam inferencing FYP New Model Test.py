import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

#nak pakai ni kena tukar self offset dekat loader.py
options =\
    {
        'model': 'cfg/tiny-yolo-voc-1c.cfg',
        'load': 20425,  # load the weight
        'threshold': 0.60,# define threshold = how much of a factor it needs to have to draw the bounding box, higher number, harder to draw bbox
        'gpu': 0.75
    }
tfnet =TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]#bounding box different color

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

while True:
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)
    print("This is line 21 : " + str(results))
    if ret:
        for color,result in zip(colors,results):
            tl = (result['topleft']['x'], result['topleft']['y'])  # pixel coordinate
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}:{:.0f}%'.format(label,confidence*100)
            frame = cv2.rectangle(frame, tl, br, color, 2)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
        cv2.imshow('Webcam',frame)
        print('FPS {:.1f}'.format(1/time.time()-stime))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
