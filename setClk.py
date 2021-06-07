from datetime import datetime
from playsound import playsound
import openYT

def Alarm(alarmHr, alarmMin):
    while True:
        if alarmHr == datetime.now().hour and alarmMin == datetime.now().minute:
            print("playing...")
            playsound("beep.mp3")
            openYT.openYT()
            break
if __name__ == "__main__":
    alarmHr = int(input("Enter Hour: "))
    alarmMin = int(input("Enter Min: "))
    Alarm(alarmHr,alarmMin)
