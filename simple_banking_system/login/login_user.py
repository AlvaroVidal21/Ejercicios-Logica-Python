import os
import time

def login_user_fn(read_json_fn, track, delete, attemps= 0):
    if attemps == 3:
        print("Demasiados intentos fallidos")
        return (False, None)
    data = read_json_fn(track)
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    for user_data in data:
        if user_data["user"] == user and user_data["password"] == password:
            print("Bienvenido")
            return (True, user_data)
        else:
            print("Usuario o contraseña incorrectos")
            attemps += 1
            time.sleep(1)
            os.system(delete)
            return login_user_fn(read_json_fn, track, attemps)