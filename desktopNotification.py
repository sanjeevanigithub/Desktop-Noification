import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "IT'S TIME TO TAKE A BREAK",
            message = "You have spent 20 minutes using a screen.\n Now you should try to look away at something that is 20 feet away from you for a total of 20 seconds",
            timeout = 21
            #app_icon = "" 
        )
        time.sleep(20*20)
