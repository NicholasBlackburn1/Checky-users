"""
this class is where allthe code is executed when ran 
"""


import imports 
import ColorLog


def Main():

    

    ColorLog.Warning("Starting Up Check Users...")

    
    # Runs on Windows platform
    if(imports.platform.system()== 'Windows'):  
        username = imports.os.getlogin()

        ColorLog.PipeLine_Ok('Running on windows... as the user'+ ' '+str(username))
        

       # Runs on Linux platform
    if(imports.platform.system()== 'Linux'):  
        username = imports.os.getlogin()

        ColorLog.PipeLine_Ok('Running on Linux... as the user'+ ' '+str(username))
        











if __name__ == '__main__':
    Main()