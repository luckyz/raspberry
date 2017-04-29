import RPi.GPIO as GPIO, time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def RCtime(pin):
    t_carga = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):
        t_carga += 1

    return t_carga

try:
    while True:
        print RCtime(12)
        if RCtime(12) > 4000:
            GPIO.output(11, True)
        else:
            GPIO.setup(11, False)

except KeyboardInterrupt:
    print '\n\n[ Execution aborted ]'
except ValueError:
    print '\n[ Unexpected value ]'
except IndexError:
    print '\n[ Index out of range ]'
except TypeError:
    print '\n[ Only 0 or 1 number required ]'
finally:
    print '\nCleaning pins...'
    GPIO.cleanup()
