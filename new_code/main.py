from connect_gpio import *

set_gpio()
def on_off(gpio, mode):
    GPIO.output(int(gpio), int(mode))

while True:
    (gpio, mode) = input("gpio, mode").split()
    on_off(gpio, mode)
    
