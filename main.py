from admin import adminInterface
from user import userInterface
from loginPage import loginPage

def main():
    login_instance = loginPage()
    login_instance.run() # run the login widow

    username = login_instance.get_user_info() # store the username returned in a variable
    
    login_instance.login_window.destroy() # exit the login window
    if username == "ADMIN": # the username of the only account with admin privilege
        admin_interface = adminInterface()
        admin_interface.changeUserName(username) # pass the username to the function 
        admin_interface.run()
    else:
        user_interface = userInterface()
        user_interface.changeUserName(username) # pass the username to the function 
        user_interface.run()
        
if __name__ == "__main__":
    main()