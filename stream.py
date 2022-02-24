import numpy as np
import cv2 as cv
import trackpy as tp
import pims
cap = cv.VideoCapture(0)
diameter_of_cells = 13
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)
    pimFrame = pims.frame.Frame(gray)
    print("1: ")
    print(type(pimFrame))
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    dataFrame = tp.locate(pimFrame, 11, invert=True, minmass=200)
    npFrame = tp.annotate(dataFrame,pimFrame)
    np_array = np.array(npFrame)
    # gray = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',np_array)
    if cv.waitKey(1) == ord('q'):
        print("break")
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()