import webbrowser
import time

total_count = 10
count = 0

print("This program started on " +time.ctime() + " and will run for 5 hours.")
while (count < total_count):
    time.sleep(1800)
    webbrowser.open("www.youtube.com/watch?v=XatesnI2dcg")
    count = count +1
