import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

option = {
    'model': 'cfg/yolov2.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.3,
    'gpu': 1.0
}
tfnet = TFNet(option)

img = cv2.imread('sample_img/sample_dog.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
# result.shape
# print(result.shape)
# cv2.imshow('result', result)
for i in range(len(result)):
    tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
    br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
    label = result[i]['label']

    img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

plt.imshow(img)
plt.show()