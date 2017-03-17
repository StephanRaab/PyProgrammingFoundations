import webbrowser
import time

print("How many breaks today?")
break_count = int(input())
total_breaks = 0

print("This program started at " + time.ctime())
while total_breaks < break_count:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=BYvhhMjW32k")
    total_breaks += 1
