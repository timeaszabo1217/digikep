import numpy as np
import cv2

wasBordered = False
key = cv2.waitKey(5000)

img = np.ndarray((480, 640, 3), np.uint8)
img.fill(255)

cv2.circle(img, (320, 100), 40, (181, 138, 159), 2)
cv2.circle(img, (300, 100), 10, (138, 181, 148), 2)
cv2.circle(img, (340, 100), 10, (138, 181, 148), 2)
cv2.circle(img, (298, 98), 5, (138, 181, 148), -1)
cv2.circle(img, (338, 98), 5, (138, 181, 148), -1)
cv2.circle(img, (320, 120), 8, (138, 181, 148), 2)
cv2.rectangle(img, (310, 110), (330, 120), (255, 255, 255), -1)
cv2.line(img, (320, 140), (320, 300), (181, 138, 159), 2)
cv2.line(img, (320, 300), (300, 480), (181, 138, 159), 2)
cv2.line(img, (320, 300), (340, 480), (181, 138, 159), 2)
cv2.line(img, (320, 200), (260, 200), (181, 138, 159), 2)
cv2.line(img, (260, 200), (250, 130), (181, 138, 159), 2)
cv2.line(img, (320, 200), (380, 300), (181, 138, 159), 2)
cv2.putText(img, 'Szabo Timea', (30, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (138, 181, 148), 2, cv2.LINE_AA)

cv2.imshow('SzaboTimea_JJMS9M.png', img)
cv2.waitKey(0)

while True:
    key = cv2.waitKeyEx(100)
    if key == ord('L'):
        rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('SzaboTimea_JJMS9M.png', rotated)
        img = rotated

    if key == ord('R'):
        rotated2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('SzaboTimea_JJMS9M.png', rotated2)
        img = rotated2

    if key == ord('B'):
        bordered = cv2.copyMakeBorder(src=img, top=1, bottom=1, left=1, right=1,
                                      borderType=cv2.BORDER_CONSTANT)
        cv2.imshow('SzaboTimea_JJMS9M.png', bordered)
        img = bordered
        wasBordered = True

    if key == ord('E') and wasBordered is True:
        cropped = img[2:482, 2:642]
        cv2.imshow('SzaboTimea_JJMS9M.png', cropped)
        img = cropped

    if key == ord('S'):
        cv2.imwrite('SzaboTimea_JJMS9M.png', img)

    if key == ord('q'):
        cv2.destroyAllWindows()
