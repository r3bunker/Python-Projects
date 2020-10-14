import shutil
import os
import datetime as dt
from tkinter import filedialog


# set where the source of the files are
source = '/Users/RyanB/Desktop/new files/'

# set the destination path of to folder B
destination = '/Users/RyanB/Desktop/destination folder/'
files = os.listdir(source)

# set today's datetime into variable today
today = dt.datetime.now().date()


for file in os.listdir(source):
    filetime = dt.datetime.fromtimestamp(
        os.path.getctime(source + file))
    print(filetime)
    if filetime.date() == today:
        print(file + ' Needs to be copied')
        # we are saying copy the files respresented by 'i' to their new destination
        shutil.copy(source+file, destination)
    else:
        print(file + ' does not need to be copied')
