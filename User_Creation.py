import os

username = raw_input('Enter in the desired username: ')
password = raw_input('Enter in the desired password: ')

os.system('sudo useradd ' + username + ' -m -p ' + password)
# net user username password /ADD
# net user John fadf24as /ADD
