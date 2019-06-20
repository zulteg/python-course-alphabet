import json
import yaml
import pickle
import uuid
from tests_homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from tests_homework.utils import get_dump_path


class InvalidValueException(Exception):
    pass


class Serializer:
    def to_dict(self):
        pass

    @classmethod
    def from_json(cls, data):
        pass

    @classmethod
    def from_yaml(cls, data):
        pass

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_json_file(self, file_name):
        with open(get_dump_path(file_name), 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

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


class Cesar(Serializer):
    def __init__(self, name=None, garages=None, register_id=None):
        if not isinstance(name, str):
            raise ValueError("Name must be string value")

        self.name = str(name)

        if register_id:
            self.set_register_id(register_id)
        else:
            self.register_id = uuid.uuid4()

        self.garages = {}
        if garages:
            if not isinstance(garages, list):
                raise ValueError(
                    "Invalid garages value, must be list of garages")
            for garage in garages:
                self.add_garage(garage)

    def __str__(self):
        return f"Cesar {self.name} has {self.garages_count()} garages with {self.cars_count()} cars " \
            f"total cost of ${self.hit_hat()}. Register id: {self.register_id}."

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def add_car(self, car, garage=None):
        if not isinstance(car, Car):
            raise TypeError("Invalid car instance")

        if not garage:
            garage = self._get_emptiest_garage()
            if not garage:
                # print("There are no empty garages")
                return False
        else:
            if not isinstance(garage, Garage):
                raise TypeError("Invalid garage instance")

            if garage.has_owner() and garage.owner != self.register_id:
                # print("This garage has other owner")
                return False

        self.add_garage(garage)
        garage.add(car)

    def add_garage(self, garage):
        if not isinstance(garage, Garage):
            raise TypeError("Invalid instance of garage")

        if garage.number in self.garages:
            return False

        garage.set_owner(self.register_id)
        self.garages[garage.number] = garage
        return True

    def _get_emptiest_garage(self):
        garage = None
        if self.garages:
            number = max(self.garages,
                         key=lambda n: self.garages[n].places_count())
            garage = self.garages[number]
            if garage.places_count() == 0:
                garage = None
        return garage

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum([garage.cars_count() for garage in self.garages.values()])

    def hit_hat(self):
        return sum([garage.hit_hat() for garage in self.garages.values()])

    def set_register_id(self, register_id):
        self.register_id = uuid.UUID(hex=str(register_id))

    def to_dict(self):
        data = {'name': self.name, 'register_id': self.register_id,
                'garages': []}

        if isinstance(self.register_id, uuid.UUID):
            data['register_id'] = str(self.register_id)

        for garage in self.garages.values():
            data['garages'].append(garage.to_dict())

        return data

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        obj = cls(name=data['name'], register_id=data['register_id'])

        for garage_str in data['garages']:
            garage = Garage.from_json(garage_str)
            for car in garage.cars.values():
                obj.add_car(car, garage)

        return obj

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        obj = cls(name=data['name'], register_id=data['register_id'])

        for garage_str in data['garages']:
            garage = Garage.from_yaml(garage_str)
            for car in garage.cars.values():
                obj.add_car(car, garage)

        return obj


class Garage(Serializer):
    def __init__(self, town, places, owner=None, cars=None, number=None):
        if town not in TOWNS:
            raise InvalidValueException("Invalid town value")
        if not isinstance(places, int):
            raise ValueError("Places must be integer value")

        self.town = town
        self.places = int(places)

        if number:
            self.set_number(number)
        else:
            self.number = uuid.uuid4()

        if owner:
            self.set_owner(owner=owner)
        else:
            self.owner = None

        self.cars = {}
        if cars:
            if not isinstance(cars, list):
                raise ValueError("Invalid cars value, must be list of cars")
            for car in cars:
                self.add(car)

    def __str__(self):
        car_len = len(self.cars)
        return f"This garage is in {self.town}, has {car_len} / {self.places} places. " \
            f"Car total price: {self.hit_hat()}.It owner: {self.owner}"

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def set_owner(self, owner):
        if isinstance(owner, Cesar):
            self.owner = owner.register_id
        else:
            self.owner = uuid.UUID(hex=str(owner))

    def set_number(self, number):
        self.number = uuid.UUID(hex=str(number))

    def add(self, car):
        if not isinstance(car, Car):
            raise TypeError("Invalid instance of car")

        if car.number in self.cars:
            # print("This car is already added to this garage")
            return False

        if self.places <= len(self.cars):
            # print("There are no empty places in this garage")
            return False

        self.cars[car.number] = car
        return True

    def remove(self, car):
        if not isinstance(car, Car):
            raise TypeError("Invalid instance of car")

        if car.number not in self.cars:
            # print("This car is not in this garage")
            return False

        self.cars.pop(car.number, None)
        return True

    def hit_hat(self):
        return sum([
            car.price for car in self.cars.values()
        ]) if self.cars else 0

    def cars_count(self):
        return len(self.cars)

    def places_count(self):
        return self.places - self.cars_count()

    def has_owner(self):
        return True if self.owner else False

    def to_dict(self):
        data = {'number': self.number, 'town': self.town,
                'places': self.places, 'owner': self.owner, 'cars': []}

        if isinstance(self.owner, uuid.UUID):
            data['owner'] = str(self.owner)

        if isinstance(self.number, uuid.UUID):
            data['number'] = str(self.number)

        for car in self.cars.values():
            data['cars'].append(car.to_dict())

        return data

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        obj = cls(town=data['town'], places=data['places'],
                  owner=data['owner'], number=data['number'])

        for json_car in data['cars']:
            car = Car.from_json(json_car)
            obj.add(car)

        return obj

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        obj = cls(town=data['town'], places=data['places'],
                  owner=data['owner'], number=data['number'])

        for json_car in data['cars']:
            car = Car.from_yaml(json_car)
            obj.add(car)

        return obj


class Car(Serializer):
    def __init__(self, price, car_type, producer, mileage, number=None):
        if not isinstance(price, float):
            raise ValueError("Price must be float value")
        if not isinstance(mileage, float):
            raise ValueError("Mileage must be float value")
        if car_type not in CARS_TYPES:
            raise InvalidValueException("Invalid car_type value")
        if producer not in CARS_PRODUCER:
            raise InvalidValueException("Invalid producer value")

        if number:
            self.set_number(number)
        else:
            self.number = uuid.uuid4()

        self.price = float(price)
        self.car_type = car_type
        self.producer = producer
        self.mileage = float(mileage)

    def __str__(self):
        return f"This car {self.car_type} type has {self.mileage} mileage and produced by {self.producer}. " \
            f"It price ${self.price}. Car number: {self.number}"

    def __repr__(self):
        return f"Car(price={self.price}, type='{self.car_type}', producer='{self.producer}', mileage={self.mileage}, " \
            f"number='{self.number}')"

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def set_number(self, number):
        self.number = uuid.UUID(hex=str(number))

    def to_dict(self):
        return {'number': str(self.number), 'price': self.price,
                'car_type': self.car_type, 'producer': self.producer,
                'mileage': self.mileage}

    @classmethod
    def from_json(cls, data):
        if not isinstance(data, dict):
            data = json.loads(data)

        return cls(price=data['price'], car_type=data['car_type'],
                   producer=data['producer'], mileage=data['mileage'],
                   number=data['number'])

    @classmethod
    def from_yaml(cls, data):
        if not isinstance(data, dict):
            data = yaml.load(data, Loader=yaml.FullLoader)

        return cls(price=data['price'], car_type=data['car_type'],
                   producer=data['producer'],
                   mileage=data['mileage'],
                   number=data['number'])
