import random
banned_accounts = ['viper_shot', 'mcdouble', 'milk._chaker', '#,.#/*']
admins = ['v1per']
global linkCode
linkCode = 1


#this does the main user input and storage
def take_input(user, passd):
    username = user
    password = passd
    fortmated_text = f'-{username}-{password}\n'
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


def create_account(un, ps):
    global linkCode
    #un stands for username and ps stands for password
    #we define the needed variable here
    username = un
    password = ps
    friend_code = generate_friend_code()
    linkCode += random.randint(0, 9999)
    userfile = open('userstorage/user.txt', 'a')
    passfile = open('userstorage/pass.txt', 'a')
    userfile.write(f'{linkCode}-{username}\n')
    passfile.write(f'{linkCode}-{password}\n')
    userfile.close()
    passfile.close()
    


def login_account():
    ask_username = input('Whats the username: ')
    userfile = open('userstorage/user.txt', 'r')
    passfile = open('userstorage/pass.txt', 'r')
    user = ask_username

    for line in userfile.readlines():
        if user in line:
            username = user
        

    code = line[:4]

    ask_password = input(f'What the password for {username}: ')
    for line in passfile.readlines():
        if code in line:
            print('User is in the data base')
        else:
            print('User is not in the database')
    if username in admins:
        admin_func(username)
    
    if username in banned_accounts:
        print('Your account was banned')
            

#a_string = 'This is a string'
#To get the first 4 letters:

#first_four_letters = a_string[:4]
#>>> 'This'

    
    
    userfile.close()
    passfile.close()


def main():
    logcreate = input('Would you like to Sign up (s) or Sign into an account (i): ')
    if logcreate == 's':
        username = input('Please create your username: ')
        password = input('Please create your password: ')
        create_account(username, password)
    elif logcreate == 'i':
        login_account()