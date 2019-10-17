import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

#%config InlineBackend.figure_format = 'svg'

options =\
{
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load' : 8975, #load the weight
    'threshold' : 0.1, #define threshold = how much of a factor it needs to have to draw the bounding box, higher number, harder to draw bbox
    'gpu' : 0.5
}

tfnet = TFNet(options)

img = cv2.imread('Test (1).png',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
img.shape

print("This is line 21 : "+str(result))
tl=(result[0]['topleft']['x'],result[0]['topleft']['y']) #pixel coordinate
br=(result[0]['bottomright']['x'],result[0]['bottomright']['y'])
label = result[0]['label']
confidence = result[0]['confidence']
confi = int(confidence*100)


print("This is line 25 \n"+str(tl))
#print("This is line 25: conf : \n"+confi)


img = cv2.rectangle(img,tl,br,(0,255,0),3) #(0,122,0) RGB code for color of bounding box and ,10 is pixel thickness)
img = cv2.putText(img,label, tl, cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),6) #fonts in openCV
plt.imshow(img)
plt.show()


