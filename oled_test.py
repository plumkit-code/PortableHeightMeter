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
oled.display()  # 실제로 OLED 화면에 반영합니다.

oled.set_text_size(2)  # 글자 크기를 2로 설정합니다.

# OLED에 출력할 내용을 준비합니다.
text = "OLED test"
integer_value = 123
float_value = 45.67

# (0, 0) 위치에 문자열을 출력합니다.
oled.set_cursor(0, 0)
oled.println(text)
# (0, 25) 위치에 정수를 출력합니다.
oled.set_cursor(0, 25)
oled.println(str(integer_value))  # 정수를 출력하고 다음 줄로 이동합니다.
# (0, 50) 위치에 소수점 두 자리까지의 실수를 출력합니다.
oled.set_cursor(0, 50)
oled.println("{:.2f}".format(float_value))  # 실수를 형식에 맞게 출력하고 다음 줄로 이동합니다.
oled.display()  # OLED 화면에 모든 내용을 표시합니다.

