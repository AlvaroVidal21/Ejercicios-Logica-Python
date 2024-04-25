# MODULES
import os
# INTERFACES
from interfaces.interface_input import *

# FEATURES
from features.clean_interface import *

# JSON ACTION
from json_actions.json_actions import *

# ACTIONS
from actions.add_input import *
from actions.write_data import *
from actions.add_expense import *


# FILES PATH
DATA = "data/data.json"



def ingresar_gastos():
    clean_interface_fn(1)
    expense = add_input_fn()
    category = add_category_fn(read_json_fn, DATA)
    add_expense_fn(category, expense, read_json_fn, write_json_fn, DATA)
    clean_interface_fn(2)



if __name__ == '__main__':
    create_categories_fn(read_json_fn, write_json_fn, DATA)
    clean_interface_fn(1)
    total_income = interface_input_fn()
    ingresar_gastos()
    while True:
        print("¿Desea agregar otro gasto? (s/n)")
        option = input(">>>_ ").strip().lower()
        if option == "s":
            ingresar_gastos()
        elif option == "n":
            break
        else:
            print("Opción no válida.")

    # Ver estadísticas
    print("Gracias por usar el sistema de finanzas.")
    os.remove(DATA)
    exit()

    
    
    # os.remove(DATA)

    
    
