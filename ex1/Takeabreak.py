import webbrowser
import time

total_breaks = 1
break_count = 1

print("Program is started on " + time.ctime())

while (break_count <= total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/waCTh?v=ib3r6mPD3aY") #play my favourite classical song by vidya and vandana from youtube
    break_count = break_count + 1

print("No more break!!")