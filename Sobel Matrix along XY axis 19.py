import cv2

img = cv2.imread("C:/Cv pics/naruto 2.png") 

cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

sobelxy = cv2.Sobel(img_blur, cv2.CV_64F, 1, 1, ksize=5) # Combined X and Y Sobel Edge Detection
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)

cv2.destroyAllWindows()
