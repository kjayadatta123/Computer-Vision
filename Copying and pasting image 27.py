import cv2
import numpy as np

image = cv2.imread("C:\Cv pics\Image Handling 1.png")
img2 = cv2.imread("C:\Cv pics\Image Handling 1.png")

if image is None or img2 is None:
    print("Error: Unable to load one or more images.")
else:
    print(image.shape) 
    cv2.imshow("original", image)

    imageCopy = image.copy()

    cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)

    cv2.imshow('image', image)
    cv2.imshow('image copy', imageCopy)

    cropped_image = image[80:280, 150:330]
    cv2.imshow("cropped", cropped_image)

    cv2.imwrite("Cropped Image.jpg", cropped_image)

    if image.shape == img2.shape:

        dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)

        
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()



