from machine import I2C, Pin
from time import sleep
from DIYables_MicroPython_OLED import OLED_SSD1306_I2C
from picozero import DistanceSensor, Button  # picozero 라이브러리 사용

# 상수 정의
BASE_HEIGHT = 180  # 천장 높이(cm) - 센서에서 천장까지의 거리
EYE_LEFT_X = 25    # 왼쪽 눈의 X 좌표
EYE_RIGHT_X = 85   # 오른쪽 눈의 X 좌표
EYE_Y = 15         # 눈의 Y 좌표
EYE_SIZE = 20      # 눈의 크기 (정사각형)
PUPIL_SIZE = 6     # 눈동자의 크기
PUPIL_OFFSET = 7   # 눈동자 위치 오프셋

# 장치 초기화
i2c = I2C(1, scl=Pin(3), sda=Pin(2))  # I2C 통신 설정 (OLED용)
oled = OLED_SSD1306_I2C(128, 64, i2c)  # OLED 디스플레이 객체 생성
distance_sensor = DistanceSensor(echo=14, trigger=15)  # 초음파 센서 (picozero)
touch_button = Button(16, pull_up=False)  # 터치 스위치 (picozero, pull_down 설정)

# 애니메이션 변수
eye_pos = 0    # 눈동자의 현재 위치 (-3 ~ 3)
eye_dir = 1    # 눈동자 이동 방향 (1: 오른쪽, -1: 왼쪽)

def measure_distance():
    """초음파 센서로 거리를 측정하는 함수 (picozero 사용)"""
    dist_m = distance_sensor.distance  # 미터 단위로 거리 측정
    if dist_m is None:  # 측정 실패
        return -1
    return dist_m * 100  # cm 단위로 변환

def print_height(h):
    """OLED에 키를 표시하는 함수"""
    oled.clear_display()  # 화면 지우기
    
    # "Height:" 텍스트 표시
    oled.set_text_size(2)
    oled.set_cursor(0, 0)
    oled.print("Height:")
    
    # 키 값 표시 (큰 글씨)
    oled.set_text_size(3)
    oled.set_cursor(0, 30)
    oled.print("{:.1f}cm".format(h))
    
    oled.display()  # 화면에 표시
    sleep(2)  # 2초간 표시

def show_default():
    """기본 대기 화면 (귀여운 얼굴 애니메이션)"""
    global eye_pos, eye_dir
    
    oled.clear_display()
    
    # 눈 흰자 그리기 (두 개의 사각형)
    oled.draw_rect(EYE_LEFT_X, EYE_Y, EYE_SIZE, EYE_SIZE, 1)
    oled.draw_rect(EYE_RIGHT_X, EYE_Y, EYE_SIZE, EYE_SIZE, 1)
    
    # 눈동자 애니메이션 (좌우로 움직임)
    eye_pos += eye_dir
    if eye_pos < -3 or eye_pos > 3:  # 경계에 도달하면 방향 전환
        eye_dir *= -1
    
    # 눈동자 그리기 (움직이는 위치에)
    pupil_x = EYE_LEFT_X + PUPIL_OFFSET + eye_pos
    oled.fill_rect(pupil_x, EYE_Y + PUPIL_OFFSET, PUPIL_SIZE, PUPIL_SIZE, 1)
    pupil_x = EYE_RIGHT_X + PUPIL_OFFSET + eye_pos
    oled.fill_rect(pupil_x, EYE_Y + PUPIL_OFFSET, PUPIL_SIZE, PUPIL_SIZE, 1)
    
    # 입 그리기 (사각형과 가로선)
    oled.draw_rect(20, 50, 88, 10, 1)
    oled.draw_fast_hline(25, 55, 78, 1)
    
    oled.display()
    sleep(0.05)  # 애니메이션 속도 조절

# 메인 루프 (무한 반복)
while True:
    if touch_button.value == 1:  # 터치 스위치가 눌렸을 때 (picozero)
        dist = measure_distance()
        
        if dist != -1:  # 측정 성공
            height = BASE_HEIGHT - dist  # 키 = 천장높이 - 센서거리
            print_height(height)  # 키 표시
        else:  # 측정 실패
            show_default()
    else:  # 터치하지 않았을 때
        show_default()  # 기본 화면 표시

