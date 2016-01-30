'''
    Author:  Rowland DePree             User_Creation.py

    This is a program designed to create a new user account on a linux machine.  You will only have to supply a proper
    username and password when prompt to by the program.
'''
import os
import platform

username = raw_input('Enter in the desired username: ')
password = raw_input('Enter in the desired password: ')

if platform.system() == 'Linux':
    os.system('sudo useradd ' + username + ' -m -p ' + password)
else:
    print 'Your system is not supported by this program.'
