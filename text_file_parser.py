import re


def parse_item(item):
    try:
        first_index = re.search('[:] ', item).end()
        return item[first_index:]
    except AttributeError:
        return None


def separate_type_and_units(item):

    drink_type_last_index = re.search('\n\n', item).end() - 2
    if item.startswith('#'):
        first_index = 2
        drink_type = item[first_index:drink_type_last_index]
    else:
        drink_type = item[:drink_type_last_index]
    units_first_index = drink_type_last_index + 3
    return drink_type, item[units_first_index:]


def parse_drinks(items):
    specifications = items.split('\n')
    if 'Выгодное предложение' in specifications:
        is_profitable = True
    else:
        is_profitable = False
    for specification in specifications:
        if specification.startswith('Название:'):
            name = parse_item(specification)
        elif specification.startswith('Сорт:'):
            variety = parse_item(specification)
        elif specification.startswith('Цена:'):
            price = parse_item(specification)
        elif specification.startswith('Картинка:'):
            picture = parse_item(specification)
    drink_specs = {
        'name': name,
        'variety': variety,
        'price': price,
        'picture': picture,
        'is_profitable': is_profitable,
    }
    return drink_specs


def fetch_drinks(file_name):

    with open(file_name, 'r', encoding='UTF-8') as file:
        text = file.read()
    drinks = []
    split_text = text.split('\n\n\n# ')
    for specific_type_drink in split_text:
        drink_type_name, specific_type_drink_units = separate_type_and_units(specific_type_drink)
        split_specific_type_drink_units = specific_type_drink_units.split('\n\n')
        drink_info_list = []
        for drink_unit_info in split_specific_type_drink_units:
            parsed_drink_unit_info = parse_drinks(drink_unit_info)
            drink_info_list.append(parsed_drink_unit_info)
        drink_type = {
            'type': drink_type_name,
            'info': drink_info_list,
        }
        drinks.append(drink_type)
    return drinks
