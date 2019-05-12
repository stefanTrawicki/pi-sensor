from microbit import *

# The minutes in a day
DAY_LENGTH = 1440
# The threshold for the amount of time spent sleeping (should be atleast 6 hours)
SLEEP_TIME = DAY_LENGTH // 4
# The length of a minute in seconds.
MINUTE_LENGTH = 60000
# The light level threshold for get_light_state().
LIGHT_THRESHOLD = 10

# Returns the state of the light (true for on, false for off).
def get_light_state():
    # Maps the light state to a threshold.
    return display.read_light_level() >= LIGHT_THRESHOLD

# Stores the time in minutes.
minutes = 0
# Stores the time the light is off.
light_off_time = 0
# Stores the minute gone to sleep.
minute_gone_sleep = 0
# Stores the day number.
day_number = 1

while True:
    #display.scroll(light_off_time)
    # Increments the time the light is off if the light is off
    if get_light_state() == False:
        light_off_time += 1
    else:
        # If the light has been off longer than the time it takes a person to sleep then we log it.
        if light_off_time >= SLEEP_TIME:
            minute_gone_sleep = minutes - light_off_time
        # Resets the light off time.
        light_off_time = 0
    # Counts the minutes.
    minutes += 1

    if minutes > DAY_LENGTH:
        # Reset all variable and dump the minute to a file.
        with open('day{0}.txt'.format(day_number), 'w') as test:
            test.write(str(minute_gone_sleep))
        minutes = 0
        light_off_time = 0
        minute_gone_sleep = 0
        day_number += 1

    # Sleeps for a minute.
    sleep(MINUTE_LENGTH)