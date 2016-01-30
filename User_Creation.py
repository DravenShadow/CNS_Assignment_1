'''
    Author:  Rowland DePree             User_Creation.py

    This is a program designed to create a new user account on either a Windows machine or a Linux base machine.
    It takes in the username and password and then uses either the command line or terminal to make the user.  It also
    auto-detects what system you are using using the platform library.
'''
import os
import platform

username = raw_input('Enter in the desired username: ')
password = raw_input('Enter in the desired password: ')

if platform.system() == 'Windows':
    os.system('net user ' + username + ' ' + password + '/ADD')
elif platform.system() == 'Linux':
    os.system('sudo useradd ' + username + ' -m -p ' + password)
else:
    print 'Your system is not supported by this program.'
