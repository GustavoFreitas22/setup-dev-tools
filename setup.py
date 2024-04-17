from time import sleep
import threading
import os

BASEDIR = "./setup"
SDKMAN_SCRIPT = 'curl -s "https://get.sdkman.io" | bash'
VPN_PACKAGES_APT_SCRIPT = 'sudo apt-get install network-manager-l2tp network-manager-l2tp-gnome apt-transport-https ca-certificates libreswan -y'

setup = False

def loadIcon():
    while setup == False:    
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            sleep(0.1)
            print(' Loading ' +i, end = '\r')
            if setup:
                 print("\r\n Done!" )
                 break

def initSetup():
    
    setupSdkMan()
    setupL2tpVpnPackages()
    
    try:
        os.mkdir(BASEDIR)
    except FileExistsError:
        print("The setup path aready exist")
    sleep(2)

def setupL2tpVpnPackages():
    try:
        os.system(VPN_PACKAGES_APT_SCRIPT)
        print("L2tp packages instaled")
    except SystemError:
        print("error to setup vpn packages")

def setupSdkMan():
    try:
        os.system(SDKMAN_SCRIPT)
        print("sdkman installed")
    except SystemError:
        print("Error to setup SdkMan")

def main():
    print("Setup develop tools!")
    t = threading.Thread(target=loadIcon)
    t.start()
    initSetup()

main()
setup = True