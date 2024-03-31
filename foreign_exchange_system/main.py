# INTERFACE
from iu_user.interface import interface_iu
# DATA
from data_exchanges.data import exchange_data_usd

# IMPORTS
import platform
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"






def doing():
    data = exchange_data_usd
    result = interface_iu(data, delete)
    print(result)


if __name__ == '__main__':
    doing()