import cv2
import numpy as np

img = cv2.imread('scissorsgray.png',cv2.IMREAD_COLOR)

px=img[55,55]

img[55,55] = [255,255,255]

px = img[55,55]
#print(px)

px = img[100:150,100:150]
#print(px)

img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)


scissors = img[200:720,700:1000]
img[0:520,0:300] = scissors

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
