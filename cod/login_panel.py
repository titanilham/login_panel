from getpass import getpass


def login_panel(logins:list, passwords:list):
    
    # access status
    entrance = False 
    
    # login writing 
    login = input("Login: " )
    
    # password writing
    password = getpass("Password: " )
    
    # login and password verification
    try:
        if login in logins:
            if logins.index(login) == passwords.index(password):
                # gaining access
                entrance = True
    except ValueError:
        entrance = False
    
    
    return entrance

if __name__ == "__main__":
    login_panel()
    
