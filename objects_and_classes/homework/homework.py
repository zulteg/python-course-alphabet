import uuid
from typing import List

from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
"""

"""
Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
"""


class Car:
    def __init__(self, price, car_type, producer, mileage, number=None):
        assert isinstance(price, float), "Price must be float value"
        assert isinstance(mileage, float), "Mileage must be float value"
        assert car_type in CARS_TYPES, "Incorrect car_type"
        assert producer in CARS_PRODUCER, "Incorrect producer"

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
        return self.price == other.price

    def set_number(self, number):
        self.number = uuid.UUID(hex=str(number))


"""
Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
"""


class Garage:
    def __init__(self, town, places, owner=None, cars=None):
        assert town in TOWNS, "Incorrect town"
        assert isinstance(places, int), "Places must be integer value"

        self.town = town
        self.places = int(places)

        self.owner = None
        if owner:
            self.set_owner(owner)

        self.cars = {}
        if cars:
            assert isinstance(cars, list), "Invalid cars value, must be list of cars"
            for car in cars:
                self.add(car)

    def __str__(self):
        return f"This garage is in {self.town}, has {len(self.cars)}/{self.places} places. " \
               f"Car total price: {self.hit_hat()}. It owner: {self.owner}"

    def set_owner(self, owner):
        if isinstance(owner, Cesar):
            self.owner = owner.register_id
        else:
            self.owner = uuid.UUID(hex=str(owner))

    def add(self, car):
        assert isinstance(car, Car), "Invalid instance of car"

        if car.number in self.cars:
            print("This car is already added to this garage")
            return False

        if self.places <= len(self.cars):
            print("There are no empty places in this garage")
            return False

        self.cars[car.number] = car

    def remove(self, car):
        assert isinstance(car, Car), "Invalid instance of car"

        if car.number not in self.cars:
            print("The car is not in this garage")
            return False

        self.cars.pop(car.number, None)

    def hit_hat(self):
        return sum([car.price for car in self.cars.values()]) if self.cars else 0

    def cars_count(self):
        return len(self.cars)

    def places_count(self):
        return self.places - self.cars_count()

    def has_owner(self):
        return True if self.owner else False


"""
Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Cesar:
    def __init__(self, name, garages=None, register_id=None):
        assert isinstance(name, str), "Name must be string value"

        self.name = name

        if register_id:
            self.set_register_id(register_id)
        else:
            self.register_id = uuid.uuid4()

        self.garages = {}
        if garages:
            assert isinstance(garages, list), "Invalid garages value, must be list of garages"
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
        return self.hit_hat() == other.hit_hat()

    def add_car(self, car, garage=None):
        assert isinstance(car, Car), "Invalid car instance"

        if not garage:
            garage = self._get_emptiest_garage()
            if not garage:
                print("There are no empty garages")
                return False
        else:
            assert isinstance(garage, Garage), "Invalid garage instance"
            if garage.has_owner() and garage.owner != self.register_id:
                print("This garage has other owner")
                return False

        self.add_garage(garage)
        garage.add(car)

    def add_garage(self, garage):
        assert isinstance(garage, Garage), "Invalid instance of garage"

        if garage not in self.garages:
            garage.set_owner(self.register_id)
            self.garages[garage] = garage

    def _get_emptiest_garage(self):
        garage = None
        if self.garages:
            garage = max(self.garages, key=lambda g: g.places_count())
            if garage.places_count() == 0:
                garage = None
        return garage

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum([garage.cars_count() for garage in self.garages])

    def hit_hat(self):
        return sum([garage.hit_hat() for garage in self.garages])

    def set_register_id(self, register_id):
        self.register_id = uuid.UUID(hex=str(register_id))
