import time
from win10toast import ToastNotifier

def notifier():
    time.sleep(60)#we can change it's arguments to change the time between notifications like for 2 hours we can replace '60' with '7200'
    tempnotific=ToastNotifier()
    tempnotific._show_toast(title='Reminder',msg='Please take a break it\'s been two minutes',duration=5,icon_path= "E:/My Programs/Temp/time_17394781.ico")


def main():
    # asyncio.run(notifier())
    i=1
    while True:
        if i==6:break
        i+=1
        notifier()

if __name__ == "__main__":
    main()


#Example given on Win10Toast officail documentation
# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
# "Python is 10 seconds awsm!",
# icon_path="custom.ico",
# duration=10)

# toaster.show_toast("Example two",
# "This notification is in it's own thread!",
# icon_path=None,
# duration=5,
# threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)