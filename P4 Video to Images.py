import cv2
import os

video = cv2.VideoCapture('videos/video_1080_20fps.avi')
success, image = video.read()
count = 0
imdir = "images"
if not os.path.isdir(imdir):
    os.mkdir(imdir)
while success:
    cv2.imwrite('images/frame%d.jpg' % count, image)
    success, image = video.read()
    count += 1
