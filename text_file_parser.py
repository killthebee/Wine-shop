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
    for drinks_by_type in split_text:
        drinks_type_name, drinks_by_type_units = separate_type_and_units(drinks_by_type)
        split_drinks_by_type_units = drinks_by_type_units.split('\n\n')
        drink_units = [parse_drinks(drink_unit) for drink_unit in split_drinks_by_type_units]

        one_type_drinks = {
            'type': drinks_type_name,
            'units': drink_units,
        }
        drinks.append(one_type_drinks)
    return drinks
