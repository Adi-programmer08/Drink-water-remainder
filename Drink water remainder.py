from plyer import notification
import time
import win32com.client

print("Thanks for using our program!\nFeel free while you work.")

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    time.sleep(3600)
    notification.notify(
        title = "Drink Water!",
        message = "Drinking water time to time keeps you healthy.",
        app_icon = "water.ico",
        timeout = 7
    )
    speaker.Speak(" ")
    speaker.Speak("Please drink Water")
