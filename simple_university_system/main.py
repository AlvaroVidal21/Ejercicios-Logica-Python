# Json actions
from controller_json.json_actions import read_json_fn, write_json_fn

# Interface
from interface.escoger_programas_iu import escoger_programas

# Constante de la ruta del archivo de datos
DATA = "data/university_data.json"



if __name__ == '__main__':
    result = escoger_programas(DATA, read_json_fn)
    print(result)
