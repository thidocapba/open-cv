import cv2 as cv

img = cv.imread('D:\Python Project\open-cv\Photos\park.jpg')

cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations = 3)
cv.imshow('Dilated', dilated)

cv.waitKey(0)