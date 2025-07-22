from machine import I2C, Pin
from DIYables_MicroPython_OLED import OLED_SSD1306_I2C
from picozero import DistanceSensor, Button
from time import sleep

# 초음파 센서 객체 (echo 핀: 14, trigger 핀: 15)
ds = DistanceSensor(echo=14, trigger=15)

# 터치 스위치 객체 (OUT 핀: GP16)
button = Button(16, pull_up=False)

# I2C 통신 초기화 (scl: GP3, sda: GP2, 속도: 400kHz)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)

# OLED 디스플레이(128x64) 객체 생성
oled = OLED_SSD1306_I2C(128, 64, i2c)

def oled_display_center(oled, text, y_offset=0):
    x1, y1, width, height = oled.get_text_bounds(text, 0, 0)
    cursor_x = (oled.WIDTH - width) // 2
    cursor_y = ((oled.HEIGHT - height) // 2) + y_offset
    oled.set_cursor(cursor_x, cursor_y)
    oled.println(text)

while True:
    oled.clear_display()
    if button.is_pressed:
        distance_cm = int(ds.distance * 100)
        oled.set_text_size(2)
        oled_display_center(oled, f"{distance_cm}cm")
        print(f"거리: {distance_cm}cm (터치됨)")
    else:
        oled.set_text_size(2)
        oled_display_center(oled, "Waiting")
        print("터치 대기중")
    oled.display()
    sleep(0.1) 