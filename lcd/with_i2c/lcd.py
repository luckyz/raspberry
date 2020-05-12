import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Hello world", 1)
lcd.lcd_display_string("My name is", 2)
lcd.lcd_display_string("picorder", 3)
lcd.lcd_display_string("I am a Raspberry Pi", 4)
sleep(2)
lcd.lcd_clear() # clear display characters
lcd.backlight(0) # turns off display backlight
