from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.MEH)
    if button_b.is_pressed():
        display.show(Image.ANGRY)
    if accelerometer.was_gesture('shake'):
        display.show(Image.SILLY)
