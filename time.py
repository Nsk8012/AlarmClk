from datetime import datetime
from playsound import playsound
from AppKit import NSSound

alarmHr = int(input("Enter Hour: "))
alarmMin = int(input("Enter Min: "))
    
while True:
    if alarmHr == datetime.now().hour and alarmMin == datetime.now().minute:
        print("playing...")
        playsound("beep.mp3")
        break