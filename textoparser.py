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
    print(second_split)
    drinks_info = []
    for index, item in enumerate(second_split, 0):
        if item.startswith('Название'):
            variety_index = index + 1
            price_index = index + 2
            picture_index = index + 3
            is_profitable_index = index + 4

            drink_info = {}
            drink_info['name'] = parse_item(item)
            try:
                drink_info['variety'] = parse_item(second_split[variety_index])
            except AttributeError:
                pass
            drink_info['price'] = parse_item(second_split[price_index])
            drink_info['picture'] = parse_item(second_split[picture_index])
            try:
                if second_split[is_profitable_index].startswith('Выгодное'):
                    drink_info['is_profitable'] = True
            except IndexError:
                pass

            drinks_info.append(drink_info)
    return drinks_info


def fetch_drinks():

    with open('file2.txt', 'r', encoding='UTF-8') as file:
        text = file.read()

    first_split = text.split('\n\n\n# ')
    # print(first_split)

    drinks = []
    for item in first_split:
        drink = {}
        drink['type'] = parse_drinks_type(item)
        drink['info'] = parse_drinks_info(item)
        drinks.append(drink)

    return drinks