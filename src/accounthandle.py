import random
banned_accounts = ['viper_shot', 'mcdouble', 'milk._chaker', '#,.#/*']
admins = ['v1per']

#this does the main user input and storage
def take_input(user, passd):
    username = user
    password = passd
    friend_code = generate_friend_code()
    fortmated_text = f'{username},{password},{friend_code},\n'
    check_accounts(username, fortmated_text)
    f = open('usercom.txt','a')
    f.write(fortmated_text)
    f.close()
    return username, password

#this function checks the accounts for certain flags etc... admin or banned accounts
def check_accounts(user, ft):
    username = user
    formated_text = ft
    #opens up the userdata
    f = open('usercom.txt','r')
    if formated_text in f:
        print('Username already exsits')

    #this is the sub area for list checking
    if username in banned_accounts:
        print('Your account was banned')
    elif username in admins:
        #trigger the admin function
        admin_func(username)
    f.close()


#this function will generate the users friend code and send to to the take_input function
def generate_friend_code():
    fc = random.randint(0,9999)
    return(fc)

def admin_func(wa):
    #wa stand for which_admin
    which_admin = wa
    admin_pass = 'v1per'
    ask = input(f'What is the password{which_admin}admin account: ')
    if ask == admin_pass:
        print(f'Welcome{which_admin}')
    else:
        print('Wrong password :(')