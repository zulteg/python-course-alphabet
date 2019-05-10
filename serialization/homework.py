import os
import uuid
import random
import json
import yaml
import pickle
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from homework4 import Cesar, Garage, Car

"""
Для попереднього домашнього завдання.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""


def get_dump_path(file_name):
    base_path = 'dumps'
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    return f"{base_path}/{file_name}"


def separator():
    print("\n" + 30 * "-" + "\n")


class CesarAdv(Cesar):
    def to_dict(self):
        data = {'name': self.name, 'register_id': self.register_id, 'garages': []}

        if isinstance(self.register_id, uuid.UUID):
            data['register_id'] = str(self.register_id)

        for garage in self.garages.values():
            data['garages'].append(garage.to_dict())

        return data

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_json_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        obj = cls(name=data['name'], register_id=data['register_id'])

        for garage_str in data['garages']:
            garage = GarageAdv.from_json(garage_str)
            for car in garage.cars.values():
                obj.add_car(car, garage)

        return obj

    @classmethod
    def from_json_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = json.load(f)

        return cls.from_json(data)

    def to_yaml(self):
        return yaml.dump(self.to_dict())

    def to_yaml_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            yaml.dump(self.to_dict(), f)

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        obj = cls(name=data['name'], register_id=data['register_id'])

        for garage_str in data['garages']:
            garage = GarageAdv.from_yaml(garage_str)
            for car in garage.cars.values():
                obj.add_car(car, garage)

        return obj

    @classmethod
    def from_yaml_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return cls.from_yaml(data)

    def to_pickle(self):
        return pickle.dumps(self)

    def to_pickle_file(self, file_name):
        with open(get_dump_path(file_name), 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(data):
        return pickle.loads(data)

    @staticmethod
    def from_pickle_file(file_name):
        with open(get_dump_path(file_name), 'rb') as f:
            data = pickle.load(f)

        return data


class GarageAdv(Garage):
    def to_dict(self):
        data = {'town': self.town, 'places': self.places, 'owner': self.owner, 'cars': []}

        if isinstance(self.owner, uuid.UUID):
            data['owner'] = str(self.owner)

        for car in self.cars.values():
            data['cars'].append(car.to_dict())

        return data

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_json_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        obj = cls(town=data['town'], places=data['places'], owner=data['owner'])

        for json_car in data['cars']:
            car = CarAdv.from_json(json_car)
            obj.add(car)

        return obj

    @classmethod
    def from_json_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = json.load(f)

        return cls.from_json(data)

    def to_yaml(self):
        return yaml.dump(self.to_dict())

    def to_yaml_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            yaml.dump(self.to_dict(), f)

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        obj = cls(town=data['town'], places=data['places'], owner=data['owner'])

        for json_car in data['cars']:
            car = CarAdv.from_yaml(json_car)
            obj.add(car)

        return obj

    @classmethod
    def from_yaml_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return cls.from_yaml(data)

    def to_pickle(self):
        return pickle.dumps(self)

    def to_pickle_file(self, file_name):
        with open(get_dump_path(file_name), 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(data):
        return pickle.loads(data)

    @staticmethod
    def from_pickle_file(file_name):
        with open(get_dump_path(file_name), 'rb') as f:
            data = pickle.load(f)

        return data


class CarAdv(Car):
    def to_dict(self):
        return {'number': str(self.number), 'price': self.price, 'car_type': self.car_type, 'producer': self.producer,
                'mileage': self.mileage}

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_json_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        return cls(price=data['price'], car_type=data['car_type'], producer=data['producer'], mileage=data['mileage'],
                   number=data['number'])

    @classmethod
    def from_json_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = json.load(f)

        return cls.from_json(data)

    def to_yaml(self):
        return yaml.dump(self.to_dict())

    def to_yaml_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            yaml.dump(self.to_dict(), f)

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        return cls(price=data['price'], car_type=data['car_type'], producer=data['producer'],
                   mileage=data['mileage'],
                   number=data['number'])

    @classmethod
    def from_yaml_file(cls, file_name):
        with open(get_dump_path(file_name), 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return cls.from_yaml(data)

    def to_pickle(self):
        return pickle.dumps(self)

    def to_pickle_file(self, file_name):
        with open(get_dump_path(file_name), 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle(data):
        return pickle.loads(data)

    @staticmethod
    def from_pickle_file(file_name):
        with open(get_dump_path(file_name), 'rb') as f:
            data = pickle.load(f)

        return data


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


if __name__ == '__main__':
    car1 = CarAdv(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car2 = CarAdv(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car3 = CarAdv(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))
    car4 = CarAdv(price=random.randint(5000, 50000), car_type=random.choice(CARS_TYPES),
                  producer=random.choice(CARS_PRODUCER), mileage=random.randint(1000, 5000))

    garage1 = GarageAdv(town=random.choice(TOWNS), places=2)
    garage2 = GarageAdv(town=random.choice(TOWNS), places=3)
    garage3 = GarageAdv(town=random.choice(TOWNS), places=4)

    cesar1 = CesarAdv(name="John")

    cesar1.add_car(car1, garage1)
    cesar1.add_car(car2, garage1)
    cesar1.add_car(car3, garage2)
    cesar1.add_car(car4, garage3)

    # print(car1)
    # print(car2)
    # print(car3)
    # print(car4)
    # print(garage1)
    # print(garage2)
    # print(garage3)
    # print(cesar1)

    print("\n\t ### JSON ###")
    debug_instance_json('car', car1, CarAdv)
    separator()
    debug_instance_json('garage', garage1, GarageAdv)
    separator()
    debug_instance_json('cesar', cesar1, CesarAdv)

    print("\n\t ### YAML ###")
    debug_instance_yaml('car', car1, CarAdv)
    separator()
    debug_instance_yaml('garage', garage1, GarageAdv)
    separator()
    debug_instance_yaml('cesar', cesar1, CesarAdv)

    print("\n\t ### PICKLE ###")
    debug_instance_pickle('car', car1, CarAdv)
    separator()
    debug_instance_pickle('garage', garage1, GarageAdv)
    separator()
    debug_instance_pickle('cesar', cesar1, CesarAdv)
