from microbit import *

def detect_light_change():
    return(display.get_light_level >= 100)

light_state_new = detect_light_change()

minute_gone_bed = 0

day_number = 1

while True:
    light_state_old = detect_light_change()
    if light_state_old != light_state_new:
        light_state_new = light_state_old
        if light_state_new == False:
            minute_gone_bed = minutes

    if minutes == 1440:
        minutes = 0
        with open(str(day_number)+'.csv', 'w') as test:
            test.write(str(minute_gone_bed))
        minute_gone_bed = 0
        day_number += 1

    minutes+=1
    sleep(60000)
