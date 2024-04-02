

def escoger_ciudad(data, read_json_fn):
    data = read_json_fn(data)
    cities = []
    cities_index = {}
    for element in data:
        for city in element.keys():
            cities.append(city)

    for index, city in enumerate(cities):
        index += 1
        print(f"{index}. {city}")
        cities_index[index] = city

    option = int(input("Escoge una ciudad: "))
    city_chosen = cities_index[option]

    return city_chosen

def escoger_programas(data, read_json_fn):
    data = read_json_fn(data)
    programs = []
    programs_index = {}

    for element