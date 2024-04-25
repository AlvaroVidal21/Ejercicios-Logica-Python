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


# FILES PATH
DATA = "data/data.json"








if __name__ == '__main__':
    create_categories_fn(read_json_fn, write_json_fn, DATA)
    # clean_interface_fn(1)
    # total_income = interface_input_fn()
    # expense = add_input_fn()

    
    
