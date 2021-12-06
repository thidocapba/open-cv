import cv2 as cv

# img = cv.imread('D:\Python Project\open-cv\Photos\cat.jpg')
# cv.imshow('Cat', img)

# Method 1:
def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live Video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Method 2:
def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)

# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)

# Reading Videos
capture = cv.VideoCapture('D:\Python Project\open-cv\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2)

    cv.imshow('Videos', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): # if the letter D is pressed, then break out of this loop and stop displaying the video
        break

capture.release()
cv.destroyAllWindows()
