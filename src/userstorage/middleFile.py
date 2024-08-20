import accounthandle as ah
import start
import main_game as mg

def test_condition_func():
    if ah.login_account == True:
        print('Trying to work')
        mg.test()

func = ah.login_account()