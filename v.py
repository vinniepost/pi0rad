from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time
from time import sleep

web = cv2.VideoCapture(0)

web.set(3,640)
web.set(4,480)
time.sleep(2)

def QRcodes(frame):
	decode = pyzbar.decode(frame)
	for code in decode:
		QR = str(code.data)
		#hier komt prob vergelijkingen
		print(QR)
	return decode

font = cv2.FONT_HERSHEY_SIMPLEX

while(web.isOpened()):
	ret, frame = web.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	decode = QRcodes(frame)

    for test1 in decode:
		points = test1.polygon

        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;

	n = len(hull)

	for j in range(0,n):
		cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

	barCode = str(decode.data)
	cv.putText(frame, barcode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)

	cv2.imshow('frame',frame)
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break
	elif key & 0xFF == ord('q'):
		cv2.imwrite('Capture.png', frame)

web.release()
cv.destroyAllWindows()
