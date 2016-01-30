"""
    Author:  Rowland DePree             User_Creation.py

    This is a program designed to create a new user account on a linux machine.  You will only have to supply a proper
    username and password when prompt to by the program.
"""
import os
import platform


def main():
    """
    Main program
    :return:
    """
    username = raw_input('Enter in the desired username: ')
    password = raw_input('Enter in the desired password: ')

    if platform.system() == 'Linux':
        os.system('sudo useradd ' + username + ' -m -p ' + password)
    else:
        print 'Error: Your system is not designed to be use with this program!'


# Runs the main program
if __name__ == '__main__':
    main()
