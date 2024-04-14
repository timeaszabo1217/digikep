import cv2
import numpy as np

img = cv2.imread('car_numberplate_rs.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
img = cv2.dilate(img, kernel)
img = cv2.erode(img, kernel)
img = cv2.erode(img, kernel)
img = cv2.dilate(img, kernel)

img = cv2.GaussianBlur(img, (5, 5), 4)

b, g, r = cv2.split(img)

g_b_max = cv2.max(g, b)

r = cv2.subtract(r, g_b_max)

_, thresholded = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.drawContours(gray, contours, -1, (0, 0, 255), 2)

cv2.imshow('SzaboTimea_JJMS9M', gray)
cv2.imwrite('SzaboTimea_JJMS9M.png', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()