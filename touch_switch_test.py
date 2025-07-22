from picozero import Button
from time import sleep

# TTP223B 터치 스위치의 OUT 핀을 GP16에 연결했다고 가정합니다.
button = Button(16, pull_up=False)  # TTP223B는 보통 풀다운이 맞음

while True:
    if button.is_pressed:
        print("터치됨")  # 터치하면 출력
    else:
        print("터치 안됨")  # 터치하지 않으면 출력
    sleep(0.1)  # 0.1초마다 상태 확인