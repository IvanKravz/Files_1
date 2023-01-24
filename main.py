
# Задача №1

with open('Menu.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        meal = line.strip()
        sum_ingridients = int(f.readline())
        ingridients = []
        for i in range(sum_ingridients):
            emp = f.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            ingridients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                })
        f.readline()
        cook_book[meal] = ingridients
print(cook_book)

# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            dict_dishes[ingridient['ingredient_name']] = {'measure': ingridient['measure'],
                                                        'quantity': int(ingridient['quantity']) * person_count,
                                                        }
    return dict_dishes
res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(res)

# Задача №3
#Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)

dict_sum = {}
dict_text = {}

def name_files(name):
    with open(name, 'r', encoding='utf-8') as f:
        name_ = name
        sum_str = 0
        str_ = []
        for line in f:  # подсчет строк в файле
            sum_str += 1
            str_.append(line)
            dict_text[name] = str_
        return dict_sum.setdefault(name, sum_str)

name_files('1.txt')
name_files('2.txt')
name_files('3.txt')

import operator
sorted_dict = dict(sorted(dict_sum.items(), key=operator.itemgetter(1)))  #сортируем dict_text по значениям

with open('Text.txt', 'w', encoding='utf-8') as f:
    for key, value in sorted_dict.items():
        name_f = f.write(f"{key}\n")
        values_str = f.write(f"{value}\n")
        for i in dict_text[key]:
            text = i.strip()
            f.write(f"{text}\n")

# print(dict_sum)
# print(dict_text)
# # print(sorted_dict)

