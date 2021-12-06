import cv2 as cv
# Reading Images
# img = cv.imread('D:\Python Project\open-cv\Photos\cat_large.jpg')

# cv.imshow('Cat', img)

#cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('D:\Python Project\open-cv\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Videos', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # if the letter D is pressed, then break out of this loop and stop displaying the video
        break

capture.release()
cv.destroyAllWindows()


