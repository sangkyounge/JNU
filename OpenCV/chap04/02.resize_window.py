import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255)                                 # 모든 원소에 255 지정

title1, title2 = "AUTOSIZE", "NORMAL"           # 윈도우 이름 변수
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)    # 윈도우 생성 - 크기 변경 불가!!
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)      # 크기 변경 가능!!

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()                         # 열린 모든 윈도우 제거

# 윈도우 창은 같이 커지지만 흰색 원소는 다 안채워짐(AUTOSIZE일 경우!!!!!)