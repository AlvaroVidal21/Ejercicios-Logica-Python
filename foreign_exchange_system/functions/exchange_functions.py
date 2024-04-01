

def exchange_to_dollars(exchange_input:str, exchange_output:str, exchange_size:float, exchange_dictionary:dict)-> float:
    

    exchange_input_to_dollars = exchange_dictionary[exchange_input]
    exchange_output_to_dollars = exchange_dictionary[exchange_output]

    exchange = round((exchange_size * exchange_input_to_dollars) / exchange_output_to_dollars, 2)

    return exchange