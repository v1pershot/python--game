
banned_accounts = ['viper_shot', 'mcdouble', 'milk._chaker', '#,.#/*']
admins = ['v1per']
def take_input(user, passd):
    username = user
    password = passd
    fortmated_text = f'{username},{password},\n'
    check_accounts(username, fortmated_text)
    f = open('test.txt','a')
    f.write(fortmated_text)
    f.close()
    return username, password

def check_accounts(user, ft):
    username = user
    formated_text = ft
    f = open('test.txt','r')
    if formated_text in f:
        print('Username already exsits')
    if username in banned_accounts:
        print('Your account was banned')
    elif username in admins:
        #trigger the admin function which has not been made yet
        print('Hello admin')
