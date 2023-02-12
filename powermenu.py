import os
import sys

action = input("""
[1] > lock 
[2] > reboot
[3] > shutdown

powermenu> """)

if action == "1" or action == "lock" or action == action.capitalize() or action == action.upper():
    os.system("betterlockscreen -l blur")
elif action == "2" or action == "reboot" or action == action.capitalize() or action == action.upper():
    os.system("clear")
    action=input("Are U sure (y/n) : ")

    if action == "" or action != "Y" or action != "y":
        sys.exit(0)
    else:
        os.system("sudo reboot")
elif action == "3" or action == "shutdown" or action == action.capitalize() or action == action.upper():
    os.system("clear")
    action = input("Are U sure (y/n) : ")

    if action == "" or action != "Y" or action != "y":
        sys.exit(0)
    else:
        os.system("sudo shutdown now ")
else:
    sys.exit(0)





        


