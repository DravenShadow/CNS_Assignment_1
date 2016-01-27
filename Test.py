import win32net

user = {'name': 'Test'}
user['passowrd'] = 'test'
user['password_age'] = 1
user['priv'] = 1
user['home_dir'] = r'C:\Users\depre\Documents'
user['comment'] = 'none'
user['flags'] = 0
user['script_path'] = 'none'

win32net.NetUserAdd('none', 1, user)
