from time import sleep
import threading
import os

SDKMAN_SCRIPT = 'curl "https://get.sdkman.io" | bash'
VPN_PACKAGES_APT_SCRIPT = 'sudo apt-get install network-manager-l2tp network-manager-l2tp-gnome apt-transport-https ca-certificates libreswan -y'
INTELLIJ_SCRIPT = 'sudo snap install intellij-idea-community --classic'
NVM_SCRIPT = 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash'
DBEAVER_SCRIPT = 'sudo snap install dbeaver-ce'
GO_SCRIPT_INSTALL = 'sudo snap install go --classic'
VSCODE_SCRIPT_INSTALL = 'sudo snap install code --classic'

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
    setupIntellij()
    setupNvm()
    setupDbeaver()
    setupGolang()
    setupVSCode()

def setupVSCode():
    try:
        os.system(VSCODE_SCRIPT_INSTALL)
        print('Visual Studio Code setup is success!')
    except SystemError:
        print("Error to setup Visual Studio Code")

def setupGolang():
    try:
        os.system(GO_SCRIPT_INSTALL)
        os.system('go version')
        print('Go setup is success!')
    except SystemError:
        print("Error to setup golang")

def setupL2tpVpnPackages():
    # try:
    #     os.system(VPN_PACKAGES_APT_SCRIPT)
    #     print("L2tp packages instaled")
    # except SystemError:
    #     print("error to setup vpn packages")
    sleep(3)
    
def setupIntellij():
    try:
        os.system(INTELLIJ_SCRIPT)
        print("Intellij installed")
    except SystemError:
        print("Error to setup Intellij")

def setupSdkMan():
    try:
        os.system(SDKMAN_SCRIPT)
        print("sdkman installed")
    except SystemError:
        print("Error to setup SdkMan")

def setupNvm():
    try:
        os.system(NVM_SCRIPT)
        print("NVM installed")
    except SystemError:
        print("Error to setup NVM")

def setupDbeaver():
    try:
        os.system(DBEAVER_SCRIPT)
        print("Dbeaver installed")
    except SystemError:
        print("Error to setup Dbeaver")

def main():
    print("Setup develop tools!")
    t = threading.Thread(target=loadIcon)
    t.start()
    initSetup()

main()
setup = True