#image rotation
import cv2


path = r"C:\Users\YAZHINI\Pictures\Screenshots\Screenshot_20230130_183052.png"


src = cv2.imread(path)


window_name = 'Image'


image = cv2.rotate(src, cv2.ROTATE_180)


cv2.imshow(window_name, image)
cv2.waitKey(0)
