import random
from tests_homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from tests_homework.models import Cesar, Garage, Car
from tests_homework.utils import separator, debug_instance_json, \
    debug_instance_pickle, debug_instance_yaml

if __name__ == '__main__':
    car1 = Car(price=random.uniform(5000, 50000),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(1000, 5000))
    car2 = Car(price=random.uniform(5000, 50000),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(1000, 5000))
    car3 = Car(price=random.uniform(5000, 50000),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(1000, 5000))
    car4 = Car(price=random.uniform(5000, 50000),
               car_type=random.choice(CARS_TYPES),
               producer=random.choice(CARS_PRODUCER),
               mileage=random.uniform(1000, 5000))

    garage1 = Garage(town=random.choice(TOWNS), places=2)
    garage2 = Garage(town=random.choice(TOWNS), places=3)
    garage3 = Garage(town=random.choice(TOWNS), places=4)

    cesar1 = Cesar(name="John")

    cesar1.add_car(car1, garage1)
    cesar1.add_car(car2, garage1)
    cesar1.add_car(car3, garage2)
    cesar1.add_car(car4, garage3)

    print("\n\t ### JSON ###")
    debug_instance_json('car', car1, Car)
    separator()
    debug_instance_json('garage', garage1, Garage)
    separator()
    debug_instance_json('cesar', cesar1, Cesar)

    print("\n\t ### YAML ###")
    debug_instance_yaml('car', car1, Car)
    separator()
    debug_instance_yaml('garage', garage1, Garage)
    separator()
    debug_instance_yaml('cesar', cesar1, Cesar)

    print("\n\t ### PICKLE ###")
    debug_instance_pickle('car', car1, Car)
    separator()
    debug_instance_pickle('garage', garage1, Garage)
    separator()
    debug_instance_pickle('cesar', cesar1, Cesar)
