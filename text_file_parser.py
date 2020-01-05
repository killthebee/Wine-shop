import re


def parse_item(item):
    first_index = re.search('[:] ', item).end()
    return item[first_index:]


def parse_drinks_type(item):

    drink_type_last_index = re.search('\n\n', item).end() - 2
    if item.startswith('#'):
        first_index = 2
        drink_type = item[first_index:drink_type_last_index]
    else:
        drink_type = item[:drink_type_last_index]
    return drink_type


def parse_drinks_info(item):

    second_split = item.split('\n')
    drinks_info = []
    for index, item in enumerate(second_split, 0):
        if item.startswith('Название'):

            variety_index = index + 1
            price_index = index + 2
            picture_index = index + 3
            is_profitable_index = index + 4

            name = parse_item(item)
            try:
                variety = parse_item(second_split[variety_index])
            except AttributeError:
                variety = None
            price = parse_item(second_split[price_index])
            picture = parse_item(second_split[picture_index])
            try:
                if second_split[is_profitable_index].startswith('Выгодное'):
                    is_profitable = True
                else:
                    is_profitable = None
            except IndexError:
                is_profitable = None

            drink_info = {
                'name': name,
                'variety': variety,
                'price': price,
                'picture': picture,
                'is_profitable': is_profitable,
            }

            drinks_info.append(drink_info)

    return drinks_info


def fetch_drinks(file_name):

    with open(file_name, 'r', encoding='UTF-8') as file:
        text = file.read()

    first_split = text.split('\n\n\n# ')

    drinks = []
    for item in first_split:
        drink = {}
        drink['type'] = parse_drinks_type(item)
        drink['info'] = parse_drinks_info(item)
        drinks.append(drink)

    return drinks