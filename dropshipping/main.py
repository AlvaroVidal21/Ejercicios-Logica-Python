# INTERFACES
from interfaces.interface_login import *
from interfaces.interface_options import *
from interfaces.interface_shipping import *
# JSON
from json_controller.json_actions import *
# LOGINS
from login.create_account import *
# FEATURES
from features.clean_interface import *
from features.tracker_generator import *
# ACTIONS
from actions.cost_value import *
from actions.calculate_date import *

#PATHS
USER_DATA  = 'data/user_data.json'





if __name__ == '__main__':
    """
    csv -> user_name, addressee_details_list, peso, precio, fecha_envio, fecha_llegada
    """

    # INTERFACE LOGIN
    option = interface_login_fn(clean_interface_fn)
    if option == 1:
        user_name = login_account_fn(read_json_fn, USER_DATA, clean_interface_fn)
    elif option == 2:
        create_account_fn(read_json_fn, write_json_fn, USER_DATA, clean_interface_fn)
    else:
        exit()

    # INTERFACE OPTIONS
    clean_interface_fn(1.5)
    option = interface_options_fn()
    if option == 1:
        print("Enviar paquete\n")
        addressee_details_list = addressee_details_fn()
        """
        addressee_details_list = [name, last_name, city, country]
        """
        tracker_id = tracker_generator_fn()
        weight, days = input_weight_fn()
        total_cost = cost_value_fn(weight, days)
        fecha_envio, fecha_llegada = calculate_date_fn(days)


    else:
        exit()

    

