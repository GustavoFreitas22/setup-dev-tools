from time import sleep
import threading

setup = False

def loadIcon():
    while setup == False:    
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            sleep(0.1)
            print(' Loading ' +i, end = '\r')
            if setup:
                 print("\r\n Done!")
                 break

def initSetup():
    sleep(5)

def main():
    print("Setup develop tools!")
    t = threading.Thread(target=loadIcon)
    t.start()
    initSetup()

main()
setup = True