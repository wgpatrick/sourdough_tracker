import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print("Hello World")
    time.sleep(1.0)
    led.value = False
    time.sleep(0.5)
