import cv2
import numpy as np

img = cv2.imread("D:/Raw Footage.mp4")

rows,cols,ch = video.shape

pts1 = np.float32([[56,65],[305,52],[28,700],[389,390]])

pts2 = np.float32([[100,50],[900,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(cols, rows))

cv2.imshow('Transformed Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
