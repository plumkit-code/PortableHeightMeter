from picozero import Button, pico_led
from time import sleep

# TTP223B 터치 스위치의 OUT 핀을 GP16에 연결했다고 가정합니다.
button = Button(16, pull_up=False)  # TTP223B는 보통 풀다운이 맞음

led_state = False  # LED 상태 저장
prev_pressed = False  # 이전 버튼 상태 저장

while True:
    if button.is_pressed:
        if not prev_pressed:  # 이전에 안 눌렸다가 지금 눌림(엣지 검출)
            led_state = not led_state  # 상태 토글
            if led_state:
                pico_led.on()
            else:
                pico_led.off()
            print("터치됨 (LED 토글)")
        prev_pressed = True
    else:
        prev_pressed = False
        print("터치 안됨")
    sleep(0.1)  # 0.1초마다 상태 확인