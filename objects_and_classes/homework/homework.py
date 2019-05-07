import uuid
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
"""

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
    def __init__(self, name=None, garages=None):
        self.register_id = uuid.uuid4()

        try:
            name = str(name)
        except ValueError:
            raise ValueError("Invalid name value")
        self.name = name

        self.garages = {}
        if garages:
            if not isinstance(garages, list):
                raise ValueError("Invalid garages value, must be list of garages")
            for garage in garages:
                self.add_garage(garage)

    def __str__(self):
        return f"Cesar {self.name} has {self.garages_count()} garages with {self.cars_count()} cars " \
               f"total cost of ${self.hit_hat()}. Register id: {self.register_id}."

    def __lt__(self, other):
        if not isinstance(other, Cesar):
            raise TypeError("Unsupported compare instances")
        return self.hit_hat() < other.hit_hat()

    def __le__(self, other):
        if not isinstance(other, Cesar):
            raise TypeError("Unsupported compare instances")
        return self.hit_hat() <= other.hit_hat()

    def __gt__(self, other):
        if not isinstance(other, Cesar):
            raise TypeError("Unsupported compare instances")
        return self.hit_hat() > other.hit_hat()

    def __ge__(self, other):
        if not isinstance(other, Cesar):
            raise TypeError("Unsupported compare instances")
        return self.hit_hat() >= other.hit_hat()

    def __eq__(self, other):
        if not isinstance(other, Cesar):
            raise TypeError("Unsupported compare instances")
        return self.hit_hat() == other.hit_hat()

    def add_car(self, car, garage=None):
        if not isinstance(car, Car):
            raise TypeError("Invalid car instance")

        if not garage:
            garage = self._get_emptiest_garage()
            if not garage:
                print("There are no empty garages")
                return False
        else:
            if not isinstance(garage, Garage):
                raise TypeError("Invalid garage instance")

            if garage.has_owner() and garage.owner != self.register_id:
                print("This garage has other owner")
                return False

        self.add_garage(garage)
        garage.add(car)

    def add_garage(self, garage):
        if not isinstance(garage, Garage):
            raise TypeError("Invalid instance of garage")

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
        if town not in TOWNS:
            raise Exception("Invalid town value")
        self.town = town

        try:
            self.places = int(places)
        except ValueError:
            raise ValueError("Invalid places value")

        if not owner:
            self.owner = None
        else:
            self.set_owner(owner=owner)

        self.cars = {}
        if cars:
            if not isinstance(cars, list):
                raise ValueError("Invalid cars value, must be list of cars")
            for car in cars:
                self.add(car)

    def __str__(self):
        return f"This garage is in {self.town}, has {len(self.cars)}/{self.places} places. " \
               f"Car total price: {self.hit_hat()}. It owner: {self.owner}"

    def set_owner(self, owner):
        if isinstance(owner, Cesar):
            self.owner = owner.register_id
        else:
            try:
                self.owner = uuid.UUID(hex=str(owner))
            except ValueError:
                raise ValueError("Invalid owner value")

    def add(self, car):
        if not isinstance(car, Car):
            raise TypeError("Invalid instance of car")

        if self.places <= len(self.cars):
            print("There are no empty places in this garage")
            return False

        if car.number in self.cars:
            print("This car is already added to this garage")
        else:
            self.cars[car.number] = car

    def remove(self, car):
        if not isinstance(car, Car):
            raise TypeError("Invalid instance of car")

        if car.number not in self.cars:
            print("This car is not in this garage")
        else:
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
        if not number:
            self.number = uuid.uuid4()
        else:
            self.set_number(number=number)

        try:
            self.price = float(price)
        except ValueError:
            raise ValueError("Invalid price value")

        if car_type not in CARS_TYPES:
            raise Exception("Invalid type value")
        self.car_type = car_type

        if producer not in CARS_PRODUCER:
            raise Exception("Invalid producer value")
        self.producer = producer

        try:
            self.mileage = float(mileage)
        except ValueError:
            raise ValueError("Invalid mileage value")

    def __str__(self):
        return f"This car {self.car_type} type has {self.mileage} mileage and produced by {self.producer}. " \
               f"It price ${self.price}. Car number: {self.number}"

    def __repr__(self):
        return f"Car(price={self.price}, type='{self.car_type}', producer='{self.producer}', mileage={self.mileage}, " \
               f"number='{self.number}')"

    def __lt__(self, other):
        if not isinstance(other, Car):
            raise TypeError("Unsupported compare instances")
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Car):
            raise TypeError("Unsupported compare instances")
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Car):
            raise TypeError("Unsupported compare instances")
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Car):
            raise TypeError("Unsupported compare instances")
        return self.price >= other.price

    def __eq__(self, other):
        if not isinstance(other, Car):
            raise TypeError("Unsupported compare instances")
        return self.price == other.price

    def set_number(self, number):
        try:
            self.number = uuid.UUID(hex=str(number))
        except ValueError:
            raise ValueError("Invalid number value")
