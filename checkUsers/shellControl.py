"""
this is for managin and handing shellcontrol from python to windows or linux 

"""

import imports 

class shellControl(object):


    def installWinget(self):
        imports.os.system("powershell -command"+" "+"iwr -outf Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"+" "+"https://github.com/microsoft/winget-cli/releases/download/v1.0.11692/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle""")