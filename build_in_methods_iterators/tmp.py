from pprint import pprint
import sys
import string
import random


def format_item(item):
    if 'name' in item:
        item['name'] = item.get('name').capitalize()
    return item


def rm_item_keys(item, keys):
    for key in keys:
        item.pop(key, None)
    return item


data = [{'age': 43, 'name': 'denis'}, {'age': 49, 'name': 'Roman'}, {'age': 36}, {'age': 47, 'name': 'spike'},
        {'age': 31, 'name': 'SuperMan'}, {'age': 49}, {'age': 37, 'name': 'claus'}, {'age': 55, 'name': 'Frank'},
        {'age': 83, 'name': 'homer'}]

# data = [{'age': 43, 'name': 'denis', 'sex': 'male'}, {'age': 49, 'name': 'Roman', 'sex': 'male'},
#         {'age': 36, 'name': 'Godzilla', 'sex': 'male'}, {'age': 47, 'name': 'spike', 'sex': 'female'},
#         {'age': 31, 'name': 'SuperMan', 'sex': 'female'}, {'age': 49, 'name': 'Batman', 'sex': 'male'},
#         {'age': 37, 'name': 'claus', 'sex': 'male'}, {'age': 55, 'name': 'Frank', 'sex': 'female'},
#         {'age': 83, 'name': 'homer', 'sex': 'male'}]

# pprint(data)

new_data = [{key: value.capitalize() if key == 'name' else value for key, value in d.items()} for d in data]

# new_data = list(map(format_item, data))
pprint(new_data)
# pprint([{**item, 'name': item['name'].title()} for item in data if item.get('name', None)])


redundant_keys = ['age', 'sex']


# new_data = [rm_item_keys(item, redundant_keys) for item in data]
# pprint(new_data)
# print(list({item.pop(key): item for item in data for key in redundant_keys}.values()))

# key = 'SuperMan'
# new_data = list(filter(lambda x: key in x.values(), data))
# pprint(data)
# pprint(new_data)

# data = [1, 2, 3, 8, 10, 12, 12, 23, 23, 1, 1, 2]
# print(min(data))

# data = ['So', 'the', 'normal', 'way', 'you', 'might', 'go', 'about', 'doing', 'this', 'task', 'in', 'python', 'is',
#         'using', 'a', 'basic', 'for', 'loop:']
# data = ['Year', 'has', 12, 'months']
# print(str(min(data, key=lambda x: len(str(x)))))


# data = [{'age': 43, 'name': 'Denis'}, {'age': 49, 'name': 'Roman'}, {'age': 36, 'name': 'Godzilla'},
#         {'age': 47, 'name': 'Spike'}, {'name': 'SuperMan'}, {'age': 49, 'name': 'Batman'}, {'age': 37, 'name': 'Claus'},
#         {'age': 55, 'name': 'Frank'}, {'age': 83, 'name': 'Homer'}]
# data = [{'age': 43, 'name': 'Denis'}, {'age': 49, 'name': 'Roman'}, {'age': 36, 'name': 'Godzilla'},
#         {'age': 47, 'name': 'Spike'}, {'age': 31, 'name': 'SuperMan'}, {'age': 49, 'name': 'Batman'},
#         {'age': 37, 'name': 'Claus'}, {'age': 55, 'name': 'Frank'}, {'age': 83, 'name': 'Homer'}]
# key = 'age'
# print(min(data, key=lambda x: x.get(key, sys.maxsize)))


# data = [[1, 2, 4, 6, 3, 4, 5], [], [2, 6, 7, 8], []]
# print(list(filter(lambda x: x, data)))
# print(max(list(filter(lambda x: x, data))))
# print(max(max(list(filter(lambda x: x, data)))))


# data = [97, 34, -35, -80, 77, -19, 71]
# print(data)
# print(sum(data))

def get_char_code(a):
    return ord(a)


# ch = 'A'
# ch = 'hello'
# print(sum(map(get_char_code, ch)))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generator_of_prime_numbers():
    number = 2
    while number < 200:
        if is_prime(number):
            yield number
        number += 1

# my_generator = generator_of_prime_numbers()
# data = []
# for i in range(200):
#     try:
#         data.append(next(my_generator))
#     except StopIteration:
#         break
# print(data)

# print([random.choice(string.ascii_lowercase) for i in range(20)])
# print(random.choices(string.ascii_lowercase, k=20))

# x = []
# if x == False:
#     print(True)
# else:
#     print(False)
