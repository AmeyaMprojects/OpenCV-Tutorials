import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
# img = cv2.resize(img, (0, 0), fx=0.65, fy=0.65)
if img is None: # check if image was loaded
    print(f"Error: Could not load image from ")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 50) # actually detects croners and returns their coordinates
corners = np.int16(corners) # convert to integers

for corner in corners: # draw circles on corners loop
	x, y = corner.ravel() # ravel() flattens the array
	cv2.circle(img, (x, y), 5, (255, 0, 0), 3) # draw a circle at the corner

for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()