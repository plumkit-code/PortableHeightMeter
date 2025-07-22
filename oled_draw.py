"""
이 코드는 newbiely.com에서 개발한 라즈베리파이 피코용 MicroPython 예제입니다.
이 코드는 누구나 자유롭게 사용할 수 있습니다.
자세한 설명과 회로도는 아래 링크를 참고하세요:
https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-oled-128x64
"""

from machine import I2C, Pin
from DIYables_MicroPython_OLED import OLED_SSD1306_I2C

# I2C 통신을 초기화합니다. (scl: GP3, sda: GP2, 속도: 400kHz)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)  # 사용 환경에 따라 핀 번호를 조정하세요

# OLED 디스플레이(128x64) 객체를 생성합니다.
oled = OLED_SSD1306_I2C(128, 64, i2c)

# 화면을 모두 지웁니다.
oled.clear_display()
oled.display()

# 사각형 그리기 (x=0, y=0 위치에 가로 40, 세로 25 크기의 테두리만 있는 사각형)
oled.draw_rect(0, 0, 40, 25, 1)
#oled.fill_rect(0, 0, 40, 25, 1)  # 채워진 사각형을 그리려면 이 줄의 주석을 해제하세요
oled.display()

# 원 그리기 (화면 중앙(64, 32)에 반지름 20인 채워진 원)
#oled.draw_circle(64, 32, 20, 1)  # 테두리만 있는 원을 그리려면 이 줄의 주석을 해제하세요
oled.fill_circle(64, 32, 20, 1)
oled.display()

# 삼각형 그리기 (세 꼭지점의 좌표로 테두리만 있는 삼각형)
oled.draw_triangle(80, 62, 128, 62, 104, 32, 1)
#oled.fill_triangle(80, 62, 128, 62, 104, 32, 1)  # 채워진 삼각형을 그리려면 이 줄의 주석을 해제하세요
oled.display()
