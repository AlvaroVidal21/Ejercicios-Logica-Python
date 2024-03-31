# INTERFACE
from iu_user.interface import interface_iu_input, interface_iu_output
# DATA
from data_exchanges.data import exchange_data_usd

# IMPORTS
import platform
import time
import os
# Operating system
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


# MAIN
def doing():
    data = exchange_data_usd
    # Obtenemos el input del usuario
    input_user = interface_iu_input(data)
    # Actions
    time.sleep(1.5)
    os.system(delete)
    # Mostramos el output elimnando el input
    output_user = interface_iu_output(input_user, data)
    print(output_user)

    


if __name__ == '__main__':
    doing()