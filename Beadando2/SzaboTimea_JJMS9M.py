import cv2
import numpy as np

img = cv2.imread('FCards_02_rs.jpg')

b, g, r = cv2.split(img)

res = img.copy()

max_diff = np.maximum.reduce([b, g, r]) - np.minimum.reduce([b, g, r])

key = cv2.waitKeyEx(0)

red_mask = np.zeros(img.shape[:2], np.uint8)
white_mask = np.zeros(img.shape[:2], np.uint8)
black_mask = np.zeros(img.shape[:2], np.uint8)

white_mask[((b > 140) & (g > 140) & (r > 140) & (max_diff < 50))] = 255
black_mask[((b < 80) & (g < 80) & (r < 80) & (max_diff < 25))] = 255
red_mask[((b < 60) & (g < 100) & (r > 150))] = 255

res[np.where(white_mask == 255)] = [255, 255, 255]
res[np.where(red_mask == 255)] = [0, 0, 255]
res[np.where(black_mask == 255)] = [0, 0, 0]
res[np.where((white_mask == 0) & (red_mask == 0) & (black_mask == 0))] = [0, 255, 255]

cv2.imshow('Cards', img)
cv2.imshow('Detected Cards', res)

if key > -1:
    cv2.destroyAllWindows()