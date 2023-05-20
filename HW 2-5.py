import cv2
import numpy as np

# image impoeting and resizing
img = cv2.imread("00tennisballs1-superJumbo.jpg")
img=cv2.resize(img, (1100, 650))

# HSV and gray format
img_HSV = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)
img_show = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apecify the edges of the image
edges = cv2.Canny(gray, 100, 200)

# find the coordinates of the balls
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 5.5, 150, maxRadius=49, minRadius=30)

# extracting the color of the center of the circles
centers_BGR = []
i = 0
if circles is not None:
	circles = circles[0].astype(np.uint32)

	for circle in circles:
		cv2.circle(img_show, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)
		i += 1
		centers_BGR.append(img_HSV[circle[1], circle[0]])

# determine the coordinates of the red ball
for (ii, center_BGR) in enumerate(centers_BGR):
	if int(center_BGR[0]) < 11:
		if int(center_BGR[1]) > 49 and int(center_BGR[1]) < 256:
			if int(center_BGR[2]) > 49 and int(center_BGR[2]) < 256:
				print("x coordinate:", circles[ii][0], "pixel")
				print("y coordinate:", circles[ii][1], "pixel")
				cv2.putText(img_show, "red ball", ((circles[ii][0]-46).astype(np.uint32), circles[ii][1].astype(np.uint32)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

	elif (int(center_BGR[0]) > 169) and (int(center_BGR[0]) < 181):
		if int(center_BGR[1]) > 49 and int(center_BGR[1]) < 256:
			if int(center_BGR[2]) > 49 and int(center_BGR[2]) < 256:
				print("x coordinate:", circles[ii][0], "pixel")
				print("y coordinate:", circles[ii][1], "pixel")
				cv2.putText(img_show, "red ball", ((circles[ii][0]-46).astype(np.uint32), circles[ii][1].astype(np.uint32)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# show image and red ball
cv2.imshow("Image", img_show)
cv2.waitKey(0)
cv2.destroyAllWindows()