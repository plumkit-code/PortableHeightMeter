from machine import I2C, Pin
from DIYables_MicroPython_OLED import OLED_SSD1306_I2C
import utime
from picozero import DistanceSensor
from time import sleep

# 초음파 센서 객체를 만듭니다. (echo 핀: 14, trigger 핀: 15)
ds = DistanceSensor(echo=14, trigger=15)

# I2C 통신을 초기화합니다. (scl: GP3, sda: GP2, 속도: 400kHz)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)  # 사용 환경에 따라 핀 번호를 조정하세요

# OLED 디스플레이(128x64) 객체를 생성합니다.
oled = OLED_SSD1306_I2C(128, 64, i2c)

# 화면을 모두 지웁니다.
oled.clear_display()
oled.display()  # 실제로 OLED 화면에 반영합니다.

def oled_display_center(oled, text):
    # 문자열의 크기(너비, 높이)를 구합니다.
    x1, y1, width, height = oled.get_text_bounds(text, 0, 0)

    # 화면 중앙에 오도록 커서 위치를 계산합니다.
    cursor_x = (oled.WIDTH - width) // 2
    cursor_y = (oled.HEIGHT - height) // 2
    oled.set_cursor(cursor_x, cursor_y)

    # 디스플레이에 문자열을 출력합니다.
    oled.println(text)

    # 변경된 내용을 OLED 화면에 표시합니다.
    oled.display()

while True:
    oled.clear_display()
    oled.set_text_size(3)  # 글자 크기를 2로 설정합니다.
    oled_display_center(oled, f"{int(ds.distance * 100)}cm")
    print(f"{int(ds.distance * 100)}cm")  # 거리를 "xxcm" 형태로 출력합니다.
    oled.display()  # 실제로 OLED 화면에 반영합니다.
    sleep(1)  # 1초(1000ms)마다 한 번씩 측정합니다.
