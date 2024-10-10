import numpy as np
import cv2

## switch case문을 사전(dictionary)으로 구현
switch_case = {
	ord('a'): "a키 입력",               		# ord() 함수- 문자를 아스키코드로 변환
  	ord('b'): "b키 입력",
  0x41: "A키 입력",
  int('0x42', 16): "B키 입력",          		
  2424832: "왼쪽 화살표키 입력",      		    # 
  2490368: "윗쪽 화살표키 입력",      		    # 
  2555904: "오른쪽 화살표키 입력",    		    # 
  2621440: "아래쪽 화살표키 입력"        		# 
}

image = np.ones((200,300), np.float32)
cv2.namedWindow('Keyboard Event')			# 
cv2.imshow('Keyboard Event', image)

while True:
    key = cv2.waitKeyEx(100)              # 100ms 동안 키 이벤트 대기 (0.1초)
    if key == 27: break                   # ESC 키 누르면 종료

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result =-1

cv2.destroyAllWindows()                 	# 열린 윈도우 모두 제거