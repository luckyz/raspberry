from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Call it with:
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=<ip_Address> python <filename.py>
# example: GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.1.111 python remote_gpio.py

factory = PiGPIOFactory(host='192.168.1.111')
led = LED(23, pin_factory=factory)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
