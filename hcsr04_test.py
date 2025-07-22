from picozero import DistanceSensor
from time import sleep

# 초음파 센서 객체를 만듭니다. (echo 핀: 14, trigger 핀: 15)
ds = DistanceSensor(echo=14, trigger=15)

while True:
    # ds.distance는 센서가 측정한 거리를 알려줍니다.
    # cm(센티미터)로 보고 싶으면 100을 곱해줍니다.
    print(f"{int(ds.distance * 100)}cm")  # 거리를 "3cm" 형태로 출력합니다.
    sleep(1)  # 1초(1000ms)마다 한 번씩 측정합니다.