[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe" -OutFile "c:\python-3.7.0.exe"

c:\python-3.7.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

# installs requirements for python script
pip3 install -r requirements.txt

# runs python module 
py.exe .\checkUsers

