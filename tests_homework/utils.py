import os
import random
import uuid
from tests_homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS, NAMES


def get_dump_path(file_name, base_path='fixtures'):
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    return os.path.join(base_path, file_name)


def separator():
    print("\n" + 30 * "-" + "\n")


def debug_instance_json(name, instance, cls):
    print(f"\n{name}:")
    print(instance)
    instance_str = instance.to_json()
    print(f"\n{name} to_json:")
    print(instance_str)
    instance_from_str = cls.from_json(instance_str)
    print(f"\n{name} from_json:")
    print(instance_from_str)
    instance.to_json_file(f'{name}.json')
    print(f"\n{name} from_json_file:")
    print(cls.from_json_file(f'{name}.json'))


def debug_instance_yaml(name, instance, cls):
    print(f"{name}:")
    print(instance)
    instance_str = instance.to_yaml()
    print(f"\n{name} to_yaml:")
    print(instance_str)
    instance_from_str = cls.from_yaml(instance_str)
    print(f"\n{name} from_yaml:")
    print(instance_from_str)
    instance.to_yaml_file(f'{name}.yaml')
    print(f"\n{name} from_yaml_file:")
    print(cls.from_yaml_file(f'{name}.yaml'))


def debug_instance_pickle(name, instance, cls):
    print(f"{name}:")
    print(instance)
    instance_str = instance.to_pickle()
    print(f"\n{name} to_pickle:")
    print(instance_str)
    instance_from_str = cls.from_pickle(instance_str)
    print(f"\n{name} from_pickle:")
    print(instance_from_str)
    instance.to_pickle_file(f'{name}.pickle')
    print(f"\n{name} from_pickle_file:")
    print(cls.from_pickle_file(f'{name}.pickle'))


def rnd_car_type(check_value=False):
    while True:
        value = random.choice(CARS_TYPES)
        if value != check_value:
            break
    return value


def rnd_car_producer(check_value=False):
    while True:
        value = random.choice(CARS_PRODUCER)
        if value != check_value:
            break
    return value


def rnd_town(check_value=False):
    while True:
        value = random.choice(TOWNS)
        if value != check_value:
            break
    return value


def rnd_name(check_value=False):
    while True:
        value = random.choice(NAMES)
        if value != check_value:
            break
    return value


def rnd_float():
    return random.uniform(1000, 10000)


def rnd_int():
    return random.randint(10, 50)


def rnd_uuid():
    return uuid.uuid4()
