# INTERFACES
from interfaces.interface_login import *
from interfaces.interface_options import *
# JSON
from json_controller.json_actions import *
# LOGINS
from login.create_account import *
# FEATURES
from features.clean_interface import *

#PATHS
USER_DATA  = 'data/user_data.json'





if __name__ == '__main__':

    option = interface_login_fn(clean_interface_fn)
    if option == 1:
        status_login = login_account_fn(read_json_fn, USER_DATA, clean_interface_fn)
    elif option == 2:
        create_account_fn(read_json_fn, write_json_fn, USER_DATA, clean_interface_fn)
    else:
        exit()

    clean_interface_fn(1)
    
    

