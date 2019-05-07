from microbit import *
data = []
time = 0
while True:
    xCord = str(accelerometer.get_x())
    yCord = str(accelerometer.get_y())
    zCord = str(accelerometer.get_z())
    appendString = (str(time) + ": " + xCord + "/" + yCord + "/" + zCord)
    data.append(appendString)

    if button_a.is_pressed():
        display.scroll ("A")
        with open('test.csv', 'w') as test:
            test.write(",".join(data))

    if button_b.is_pressed():
        display.scroll ("B")

    sleep(1000)
    time+=1
