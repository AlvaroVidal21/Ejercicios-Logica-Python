from iu.welcome import print_welcome
# LOGIN
from login.register import register_new_user
from login.add_user_to_data import add_new_user
from login.login_user import login_user_fn
# JSON
from controller_json.read_json import read_json_fn
from controller_json.write_json import write_json_fn

import json





def doing():
    track = "users/all_users.json"
    opcion_de_usuario = print_welcome()

    if opcion_de_usuario == 1:
        login_user_fn(read_json_fn, track)
    elif opcion_de_usuario == 2:
        nombre, apellido, dni, user, password = register_new_user()
        add_new_user(nombre, apellido, dni, user, password, read_json_fn, write_json_fn, track)


    



if __name__ == '__main__':
    doing()