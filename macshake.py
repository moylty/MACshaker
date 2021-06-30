import os
import time
import random

TIME = ""
NEWMAC = ""

class colours:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    ENDC = '\033[0m'
    YELLOW = '\033[93m'

print(colours.BLUE + ".___  ___.      ___       ______               _______. __    __       ___       __  ___  _______ .______     ")
print(colours.BLUE + "|   \/   |     /   \     /      |             /       ||  |  |  |     /   \     |  |/  / |   ____||   _  \     ")
print(colours.BLUE + "|  \  /  |    /  ^  \   |  ,----'            |   (----`|  |__|  |    /  ^  \    |  '  /  |  |__   |  |_)  |    ")
print(colours.BLUE + "|  |\/|  |   /  /_\  \  |  |                  \   \    |   __   |   /  /_\  \   |    <   |   __|  |      /     ")
print(colours.BLUE + "|  |  |  |  /  _____  \ |  `----.         .----)   |   |  |  |  |  /  _____  \  |  .  \  |  |____ |  |\  \----.")
print(colours.BLUE + "|__|  |__| /__/     \__\ \______|         |_______/    |__|  |__| /__/     \__\ |__|\__\ |_______|| _| `._____|\n")
                                                                                                               
######################

def randomize_mac() :
    #get the time
    t = time.localtime()
    TIME = time.strftime("%H:%M:%S", t)

    #change mac
    os.system("sudo macchanger -r eth0")
    print(colours.CYAN + "\nMAC address changed at " + colours.YELLOW + TIME + "\n" + colours.ENDC)
    


#interval selection
interval = input(colours.GREEN + "Enter an interval to randomise MAC at (In Minutes)\n" + colours.ENDC)

while True:
    randomize_mac()
    time.sleep(int(interval) * 60)
