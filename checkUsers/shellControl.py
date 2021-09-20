"""
this is for managin and handing shellcontrol from python to windows or linux 

"""

import imports 
import ColorLog

class shellControl(object):


    def installWinget(self):
        imports.os.system("powershell -command"+" "+"iwr -outf Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"+" "+"https://github.com/microsoft/winget-cli/releases/download/v1.0.11692/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle""")
        ColorLog.PipeLine_Ok("Done downloading Winget Time to install it...")
        ColorLog.Warning("installing winget.....")
        imports.os.system("powershell -command "+" "+"Add-AppxPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle")
        ColorLog.PipeLine_Ok("Done installing winget...")

    def installWindowsUpdate(self):
        ColorLog.Warning("Downloading windows Updates...")
        imports.os.system("powershell -command"+" "+"Get-WindowsUpdate")
        ColorLog.PipeLine_Ok("Done Downloading windows updates...")
        ColorLog.Warning("Installing windows Updates...")
        imports.os.system("powershell --command Get-WindowsUpdate -AcceptAll -Install")
        ColorLog.PipeLine_Ok("Done Installing windows updates...")

    def installFireFox(self):
        ColorLog.Warning("installing FireFox...")
        imports.os.system("winget install -e --id Mozilla.Firefox")
        ColorLog.PipeLine_Ok("Done installing FireFox...")

    def installGoogleChrome(self):
        ColorLog.Warning("installing google chrome...")
        imports.os.system("winget install -e --id Google.Chrome")
        ColorLog.PipeLine_Ok("Done isntallign google chrome ...")


    def installAdobeArobat(self):
        ColorLog.Warning("installing Adobe.AdobeAcrobatReaderDC....")
        imports.os.system("winget install -e --id Adobe.AdobeAcrobatReaderDC")
        ColorLog.PipeLine_Ok("Done isntallign Adobe.AdobeAcrobatReaderDC ...")
