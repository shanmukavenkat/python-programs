import cv2 as cv
import matplotlib.pyplot as pp
import sys
img = cv.imread(r"C:\Users\A.S.N.V.S.KOMAL\Downloads\istockphoto-183806583-170667a.jpg",1)
if img is None:
    sys.exit("Could not read the image.")
cv.imshow(r"Image",img)
