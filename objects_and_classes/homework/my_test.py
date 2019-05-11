import random
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from objects_and_classes.homework.homework import Cesar, Garage, Car

c1 = Cesar(name="2131")
c2 = Cesar(name="Naumov")
c3 = Cesar(name="Gavryl")

car1 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))
car2 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))
car3 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))
car4 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))
car5 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))
car6 = Car(price=random.uniform(5000, 50000), car_type=random.choice(CARS_TYPES),
           producer=random.choice(CARS_PRODUCER), mileage=random.uniform(1000, 5000))

garage1 = Garage(town=random.choice(TOWNS), places=2)
garage2 = Garage(town=random.choice(TOWNS), places=3)
garage3 = Garage(town=random.choice(TOWNS), places=4)
garage4 = Garage(town=random.choice(TOWNS), places=4, owner=c2, cars=[car5, car4])

# print(garage4)
# print("\n - ACTION")

garage1.add(car1)
garage2.add(car2)
garage3.add(car3)

c4 = Cesar(name="Gover", garages=[garage1])

# print("\n - GARAGES")
# print(garage1)
# print(garage2)
#
# print("\n - PRICES")
# print(garage1.hit_hat())
# print(garage2.hit_hat())

print(car1 > car2)
print(car3 == car2)
print(car3 <= car2)

c1.add_car(car1, garage1)
c2.add_car(car2, garage2)
c1.add_car(car2, garage1)
c1.add_car(car3, garage1)
c1.add_car(car3, garage2)
c1.add_car(car4, garage2)
c1.add_car(car5, garage2)
c1.add_car(car4)
c4.add_car(car6, garage2)

# print(garage2 == 123)

print(c1 > c2)
print(c1 >= c2)
print(c1 < c2)
print(c1 == c2)

# print(garage1)
# print(garage2)
# print(c1)


# print("\n - CESARS")
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print("\n - CARS")
# print(car1)
# print(car2)
# print(car3)
# print("\n - GARAGES")
# print(garage1)
# print(garage2)
# print(garage3)
