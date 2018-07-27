import cv2
import numpy as np

capture = cv2.VideoCapture('videos/20180414_151414.mp4')
size = {
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
}

codec = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('video_1080_20fps.avi', codec, 60.0, (1920, 1080))

i = 0
frame_rate_divider = 3
while (capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        if i % frame_rate_divider == 0:
            output.write(frame)
            cv2.imshow('Video downsample', frame)
            i += 1
        else:
            i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
