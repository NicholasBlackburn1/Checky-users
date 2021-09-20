"""
this class is where allthe code is executed when ran 

TODO: get linux version running to 
"""


from shellControl import shellControl
import imports 
import ColorLog


def Main():

    

    ColorLog.Warning("Starting Up Check Users...")

    
    # Runs on Windows platform
    if(imports.platform.system()== 'Windows'):  
        username = imports.os.getlogin()

        ColorLog.PipeLine_Ok('Running on windows... as the user'+ ' '+str(username))
        
        if(not username):
            ColorLog.Error("Cannot run without user being Active")
        
        if(username and imports.ctypes.windll.shell32.IsUserAnAdmin()):
            ColorLog.Warning("got Active user time to run stuff")

            # this Downloads windows updates
            ColorLog.Warning("Downlaoding Windows Updates....")
            shellControl.installWindowsUpdate(shellControl())
            ColorLog.PipeLine_Ok("Done Downlaoding Windows Updates....")
            
            # this downloads and installs winget
            ColorLog.Warning("Installing winget...")
            shellControl.installWinget(shellControl())
            ColorLog.PipeLine_Ok(" Done installing winget...")

            # This will install fire fox
            shellControl.installFireFox(shellControl())

            # this will install google chrome
            shellControl.installGoogleChrome(shellControl())

            # this will install Adobe chrome
            shellControl.installAdobeArobat(shellControl())
       # Runs on Linux platform
    if(imports.platform.system()== 'Linux'):  
        username = imports.os.getlogin()

        ColorLog.PipeLine_Ok('Running on Linux... as the user'+ ' '+str(username))

        if(not username):
            ColorLog.Error("Cannot run without user being Active")

        else:
            ColorLog.Warning("got Active user time to run stuff")
            











if __name__ == '__main__':
    Main()