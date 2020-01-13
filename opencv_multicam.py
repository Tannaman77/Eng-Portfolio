import cv2
import numpy as np

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
while(True):
	ret0, frame0 = cap0.read(320)
	ret1, frame1 = cap1.read()
	
	if (ret0):
		cv2.imshow('Cam0' , frame0)
	if (ret1):
		cv2.imshow('Cam1' , frame1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap0.release()
cap1.release()
cv2.destroyAllWindows()
