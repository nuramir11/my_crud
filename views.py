# from itertools import product
import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)


def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id +=1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id 

def created_product():
    data = get_data()
    product = ({
        'id': get_id(),
        'title': input("Введите название продукта ->"),
        'model': input('Введите модель кроссовок ->'),
        'price': int(input('Введите цену продукта ->'))
    })
    data.append(product)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return "Продукт создан"

def update_product():
    data = get_data()
    flag = False 
    id = int(input('Введите id для изменения продукта -> '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return "Нет такого продукта"
    index_ = data.index(product[0])
    user = input('Что вы хотите изменить? \n 1 - title \n 2 - model \n 3 - description \n 4 - price')
    if user == '1':
        data[index_] ['title'] = input('Введите новое название продукта -> ')
        flag = True 
    elif user == '2':
        data[index_] ['model'] = int(input('Введите модель кроссовок  -> '))
        flag = True
    elif user == '3':
        data[index_] ['description'] = int(input('Введите размер кроссовок -> '))
        flag = True
    elif user == '4':
        data[index_] ['price'] = int(input('Введите цену кроссовок -> '))
        flag = True
    else:
        return 'Такой команды нет!'

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    # return 'Файл изменен'

    if flag:
        return "UPDATE"
    else:
        return 'no uptated'


def delete_product():
    data = get_data()
    id = int(input('Введите ID для удаления ->'))
    product = list(filter(lambda x:x['id'] == id,data))
    if not product:
        return 'fed'
    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILE_PATH, 'w'))
    return "Продукт удален!"

def get_one_product():
    data = get_data()
    id = int(input('Введите id продукта'))
    product = list(filter(lambda x:x['id'] == id, data))

    if product:
        return product[0]

    else:
        return "Такого продукта нет!"
