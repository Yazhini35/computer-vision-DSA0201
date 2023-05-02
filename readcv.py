import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/YAZHINI/Pictures/Screenshots/Screenshot_20230130_183052.png"
img =  cv2.imread(path)
 
cv2.imshow("Lena",img)
cv2.waitKey(0)

