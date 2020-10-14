from datetime import datetime, time
import pytz


# get local times
portland_datetime = datetime.now(pytz.timezone('US/Pacific'))
nyc_datetime = datetime.now(pytz.timezone('US/Eastern'))
london_datetime = datetime.now(pytz.timezone('Europe/London'))

# convert time to string
portland = portland_datetime.strftime("%H:%M:%S")
nyc = nyc_datetime.strftime("%H:%M:%S")
london = london_datetime.strftime("%H:%M:%S")


def is_open(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]


if (is_open(portland, ("9:00", "17:00"))) == True:
    print("Portland HQ is open")
    if (is_open(nyc, ("9:00", "17:00"))) == True:
        print("The New York branch is open")
    elif (is_open(nyc, ("9:00", "17:00"))) == False:
        print("The New York branch is closed")
    if (is_open(london, ("9:00", "17:00"))) == True:
        print("The London branch is open")
    elif (is_open(london, ("9:00", "17:00"))) == False:
        print("The London branch is closed")
else:
    print("Portland is closed")
