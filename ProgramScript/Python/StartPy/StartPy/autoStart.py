import os
import getpass

USER_NAME = getpass.getuser()

def Add_to_strtup(file_path="E:\\Programer.py"):
    bat_path = r'' % USER_NAME
    with open(bat_path + '\\' + "open.bat", 'w+') as bat_file:
        bat_file.write(r'start "name" %s' % file_path)
        
Add_to_strtup()