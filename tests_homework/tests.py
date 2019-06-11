import unittest
import uuid
import json
import yaml
import pickle
from tests_homework.models import InvalidValueException, Cesar, Garage, Car
from tests_homework.utils import (
    rnd_car_producer,
    rnd_car_type,
    rnd_town,
    rnd_name,
    rnd_float,
    rnd_int,
    rnd_uuid,
)


class CarCases(unittest.TestCase):
    def test_init_with_invalid_price(self):
        for value in [1000, '5000', '111,23']:
            with self.assertRaises(ValueError):
                Car(value, rnd_car_type(), rnd_float(), rnd_float())

    def test_init_with_invalid_car_type(self):
        for value in ['My Type', 1000, ['Type 1', 'Type 2']]:
            with self.assertRaises(InvalidValueException):
                Car(rnd_float(), value, rnd_car_producer(), rnd_float())

    def test_init_with_invalid_car_producer(self):
        for value in ['My Producer', 1000, ['Producer 1', 'Producer 2']]:
            with self.assertRaises(InvalidValueException):
                Car(rnd_float(), rnd_car_type(), value, rnd_float())

    def test_init_with_invalid_mileage(self):
        for value in [1000, '5000', '111,23']:
            with self.assertRaises(ValueError):
                Car(rnd_float(), rnd_car_type(), rnd_car_producer(), value)

    def test_init_with_invalid_number(self):
        for value in ['some string', 1000]:
            with self.assertRaises(ValueError):
                Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                    rnd_float(), value)

    def test_set_number(self):
        car = Car(rnd_float(), rnd_car_type(), rnd_car_producer(), rnd_float())
        new_number = rnd_uuid()
        car.set_number(new_number)
        self.assertEqual(car.number, new_number)
        self.assertIsInstance(car.number, uuid.UUID)

    def test_comparison(self):
        car1 = Car(1000.0, rnd_car_type(), rnd_car_producer(), rnd_float())
        car2 = Car(2000.0, rnd_car_type(), rnd_car_producer(), rnd_float())
        car3 = Car(1000.0, rnd_car_type(), rnd_car_producer(), rnd_float())

        self.assertFalse(car1 > car2)
        self.assertTrue(car1 >= car3)
        self.assertTrue(car1 < car2)
        self.assertTrue(car1 <= car3)

    def test_json_serialize(self):
        filename = 'car.json'

        car_from_json = Car.from_json_file(filename)

        with open(f"fixtures/{filename}") as f:
            car_json = json.loads(f.read())
            car = Car(
                price=car_json.get('price'),
                car_type=car_json.get('car_type'),
                producer=car_json.get('producer'),
                mileage=car_json.get('mileage'),
                number=car_json.get('number')
            )

        self.assertEqual(car, car_from_json)

    def test_equal_method(self):
        price = rnd_float()
        car_type = rnd_car_type()
        car_producer = rnd_car_producer()
        mileage = rnd_float()
        number = rnd_uuid()

        car1 = Car(price, car_type, car_producer, mileage, number)
        car2 = Car(price, car_type, car_producer, mileage, number)
        self.assertEqual(car1, car2)

        car2 = Car(price + 1, car_type, car_producer, mileage, number)
        self.assertNotEqual(car1, car2)

        car2 = Car(price, rnd_car_type(car_type), car_producer, mileage,
                   number)
        self.assertNotEqual(car1, car2)

        car2 = Car(price, car_type, rnd_car_producer(car_producer), mileage,
                   number)
        self.assertNotEqual(car1, car2)

        car2 = Car(price, car_type, car_producer, mileage + 1, number)
        self.assertNotEqual(car1, car2)

        car2 = Car(price, car_type, car_producer, mileage, rnd_uuid())
        self.assertNotEqual(car1, car2)


class GarageCases(unittest.TestCase):
    def test_init_with_invalid_town(self):
        for value in ['My Town', 1000, ['Town 1', 'Town 2']]:
            with self.assertRaises(InvalidValueException):
                Garage(value, rnd_int())

    def test_init_with_invalid_places(self):
        for value in [100.23, 'some string', '123,22']:
            with self.assertRaises(ValueError):
                Garage(rnd_town(), value)

    def test_init_with_invalid_owner(self):
        for value in ['some string', 1000]:
            with self.assertRaises(ValueError):
                Garage(rnd_town(), rnd_int(), value)

    def test_init_with_invalid_cars(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        for value in ['My Car', car1, {'car': car1}]:
            with self.assertRaises(ValueError):
                Garage(rnd_town(), rnd_int(), rnd_uuid(), value)

    def test_set_owner(self):
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid())

        new_owner = rnd_uuid()
        garage.set_owner(new_owner)
        self.assertEqual(garage.owner, new_owner)
        self.assertIsInstance(garage.owner, uuid.UUID)

        cesar = Cesar('Test')
        garage.set_owner(cesar)
        self.assertEqual(garage.owner, cesar.register_id)
        self.assertIsInstance(garage.owner, uuid.UUID)

    def test_add_instance(self):
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid())
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        with self.assertRaises(TypeError):
            garage.add('My Car')

        with self.assertRaises(TypeError):
            garage.add([car1])

    def test_add_same_car(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1])

        before_cars = garage.cars
        self.assertFalse(garage.add(car1))
        after_cars = garage.cars
        self.assertEqual(before_cars, after_cars)

    def test_add_when_no_places(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), 1, rnd_uuid(), [car1])

        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        before_cars = garage.cars
        self.assertFalse(garage.add(car2))
        after_cars = garage.cars
        self.assertEqual(before_cars, after_cars)

    def test_add_car(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), 10, rnd_uuid(), [car1])

        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        self.assertTrue(garage.add(car2))
        self.assertTrue(car2.number in garage.cars)
        self.assertEqual(garage.cars[car2.number], car2)

    def test_remove_instance(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1])

        with self.assertRaises(TypeError):
            garage.add('My Car')

        with self.assertRaises(TypeError):
            garage.add([car1])

    def test_remove_not_existing_car(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1])

        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        before_cars = garage.cars
        self.assertFalse(garage.remove(car2))
        after_cars = garage.cars
        self.assertEqual(before_cars, after_cars)

    def test_remove_car(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), 10, rnd_uuid(), [car1])

        self.assertTrue(garage.remove(car1))
        self.assertTrue(car1.number not in garage.cars)
        self.assertEqual(garage.cars, {})

    def test_hit_hat(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1, car2])

        self.assertEqual(garage.hit_hat(), car1.price + car2.price)

        garage = Garage(rnd_town(), rnd_int(), rnd_uuid())
        self.assertEqual(garage.hit_hat(), 0)

    def test_cars_count(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1, car2])

        self.assertEqual(garage.cars_count(), 2)

    def test_places_count(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage = Garage(rnd_town(), 5, rnd_uuid(), [car1, car2])

        self.assertEqual(garage.places_count(), 3)

    def test_has_owner(self):
        garage = Garage(rnd_town(), rnd_int())
        self.assertFalse(garage.has_owner())

        garage = Garage(rnd_town(), rnd_int(), rnd_uuid())
        self.assertTrue(garage.has_owner())

    def test_pickle_serialize(self):
        filename = 'garage.pickle'

        garage_from_pickle = Garage.from_pickle_file(filename)

        with open(f"fixtures/{filename}", "rb") as f:
            garage = pickle.loads(f.read())

        self.assertEqual(garage, garage_from_pickle)

    def test_equal_method(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        town = rnd_town()
        places = rnd_int()
        owner = rnd_uuid()
        cars = [car1, car2]
        number = rnd_uuid()

        garage1 = Garage(town, places, owner, cars, number)
        garage2 = Garage(town, places, owner, cars, number)
        self.assertEqual(garage1, garage2)

        garage2 = Garage(rnd_town(town), places, owner, cars, number)
        self.assertNotEqual(garage1, garage2)

        garage2 = Garage(town, places + 1, owner, cars, number)
        self.assertNotEqual(garage1, garage2)

        garage2 = Garage(town, places, rnd_uuid(), cars, number)
        self.assertNotEqual(garage1, garage2)

        garage2 = Garage(town, places, owner, [car1], number)
        self.assertNotEqual(garage1, garage2)

        garage2 = Garage(town, places, owner, cars, rnd_uuid())
        self.assertNotEqual(garage1, garage2)


class CesarCases(unittest.TestCase):
    def test_init_with_invalid_name(self):
        for value in [1000, 11.23, False]:
            with self.assertRaises(ValueError):
                Cesar(value)

    def test_init_with_invalid_garages(self):
        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid())
        for value in ['My Garage', garage1, {'garage': garage1}]:
            with self.assertRaises(ValueError):
                Cesar(rnd_name(), [], value)

    def test_init_with_invalid_register_id(self):
        for value in [1000, 'some string']:
            with self.assertRaises(ValueError):
                Cesar(rnd_name(), [], value)

    def test_init_add_car_instance(self):
        cesar = Cesar(rnd_name())
        car = Car(rnd_float(), rnd_car_type(), rnd_car_producer(), rnd_float())

        for value in [1000, 'some string', [car]]:
            with self.assertRaises(TypeError):
                cesar.add_car(value)

    def test_init_add_car_garage_instance(self):
        cesar = Cesar(rnd_name())
        garage = Garage(rnd_town(), rnd_int(), rnd_uuid())
        car = Car(rnd_float(), rnd_car_type(), rnd_car_producer(), rnd_float())

        for value in [1000, 'some string', [garage]]:
            with self.assertRaises(TypeError):
                cesar.add_car(car, value)

    def test_init_add_car_emptiest_garage(self):
        garage1 = Garage(rnd_town(), 1, rnd_uuid())
        garage2 = Garage(rnd_town(), 2, rnd_uuid())
        garage3 = Garage(rnd_town(), 3, rnd_uuid())
        cesar = Cesar(rnd_name(), [garage1, garage2, garage3])

        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        cesar.add_car(car1)
        self.assertEqual(garage1.places_count(), 1)
        self.assertEqual(garage2.places_count(), 2)
        self.assertEqual(garage3.places_count(), 2)

        cesar.add_car(car2)
        self.assertEqual(garage1.places_count(), 1)
        self.assertEqual(garage2.places_count(), 1)
        self.assertEqual(garage3.places_count(), 2)

    def test_init_add_car(self):
        garage1 = Garage(rnd_town(), 1)
        garage2 = Garage(rnd_town(), 2)
        cesar = Cesar(rnd_name(), [garage1])

        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car3 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        cesar.add_car(car1, garage1)
        cesar.add_car(car2, garage2)
        cesar.add_car(car3, garage2)

        self.assertEqual(cesar.register_id, garage1.owner)
        self.assertEqual(cesar.register_id, garage2.owner)

        self.assertEqual(garage1.cars_count(), 1)
        self.assertEqual(garage2.cars_count(), 2)

        self.assertTrue(car1.number in garage1.cars)
        self.assertTrue(car2.number in garage2.cars)
        self.assertTrue(car3.number in garage2.cars)

    def test_init_add_garage_instance(self):
        cesar = Cesar(rnd_name())
        garage = Garage(rnd_town(), rnd_int())

        for value in [1000, 'some string', [garage]]:
            with self.assertRaises(TypeError):
                cesar.add_garage(value)

    def test_init_add_garage(self):
        garage1 = Garage(rnd_town(), rnd_int())
        garage2 = Garage(rnd_town(), rnd_int())
        cesar = Cesar(rnd_name(), [garage1])

        self.assertFalse(cesar.add_garage(garage1))
        self.assertTrue(cesar.add_garage(garage2))

        self.assertEqual(cesar.register_id, garage1.owner)
        self.assertEqual(cesar.register_id, garage2.owner)

        self.assertTrue(garage1.number in cesar.garages)
        self.assertTrue(garage2.number in cesar.garages)

    def test_garages_count(self):
        garage1 = Garage(rnd_town(), rnd_int())
        garage2 = Garage(rnd_town(), rnd_int())
        cesar = Cesar(rnd_name(), [garage1, garage2])

        self.assertEqual(cesar.garages_count(), 2)

    def test_cars_count(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car3 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1])
        garage2 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car2, car3])
        cesar = Cesar(rnd_name(), [garage1, garage2])

        self.assertEqual(cesar.cars_count(), 3)

    def test_hit_hat(self):
        car1 = Car(1000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(2000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car3 = Car(3000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())

        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1])
        garage2 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car2, car3])
        cesar = Cesar(rnd_name(), [garage1, garage2])

        self.assertEqual(cesar.hit_hat(), 6000)

    def test_set_register_id(self):
        cesar = Cesar(rnd_name())
        new_register_id = rnd_uuid()
        cesar.set_register_id(new_register_id)

        self.assertEqual(cesar.register_id, new_register_id)
        self.assertIsInstance(cesar.register_id, uuid.UUID)

    def test_comparison(self):
        car1 = Car(1000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(2000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1, car2])
        cesar1 = Cesar(rnd_name(), [garage1])

        car1 = Car(1000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(3000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1, car2])
        cesar2 = Cesar(rnd_name(), [garage1])

        car1 = Car(2000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(1000.0, rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage1 = Garage(rnd_town(), rnd_int(), rnd_uuid(), [car1, car2])
        cesar3 = Cesar(rnd_name(), [garage1])

        self.assertFalse(cesar1 > cesar2)
        self.assertTrue(cesar1 >= cesar3)
        self.assertTrue(cesar1 < cesar2)
        self.assertTrue(cesar1 <= cesar3)

    def test_yaml_serialize(self):
        filename = 'cesar.yaml'

        cesar_from_yaml = Cesar.from_yaml_file(filename)

        with open(f"fixtures/{filename}") as f:
            cesar_json = yaml.load(f.read(), Loader=yaml.FullLoader)

        garages = []
        for garage_json in cesar_json.get('garages'):
            cars = []
            for car_json in garage_json.get('cars'):
                car = Car(
                    price=car_json.get('price'),
                    car_type=car_json.get('car_type'),
                    producer=car_json.get('producer'),
                    mileage=car_json.get('mileage'),
                    number=car_json.get('number')
                )
                cars.append(car)
            garage = Garage(
                town=garage_json.get('town'),
                places=garage_json.get('places'),
                owner=garage_json.get('owner'),
                cars=cars,
                number=garage_json.get('number')
            )
            garages.append(garage)
        cesar = Cesar(
            name=cesar_json.get('name'),
            garages=garages,
            register_id=cesar_json.get('register_id')
        )

        self.assertEqual(cesar, cesar_from_yaml)

    def test_equal_method(self):
        car1 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car2 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        car3 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        garage1 = Garage(rnd_town(), rnd_int(), None, [car1, car2])
        garage2 = Garage(rnd_town(), rnd_int(), None, [car3])

        name = rnd_name()
        garages = [garage1, garage2]
        register_id = rnd_uuid()

        cesar1 = Cesar(name, garages, register_id)
        cesar2 = Cesar(name, garages, register_id)
        self.assertEqual(cesar1, cesar2)

        cesar2 = Cesar(rnd_name(name), garages, register_id)
        self.assertNotEqual(cesar1, cesar2)

        cesar2 = Cesar(name, garages, rnd_uuid())
        self.assertNotEqual(cesar1, cesar2)

        garage3 = Garage(rnd_town(), rnd_int(), None)
        car4 = Car(rnd_float(), rnd_car_type(), rnd_car_producer(),
                   rnd_float())
        cesar2 = Cesar(name, garages, register_id)
        cesar2.add_car(car4, garage3)
        self.assertNotEqual(cesar1, cesar2)

        garage3 = Garage(rnd_town(), rnd_int(), rnd_uuid())
        new_garages = [garage3]
        cesar2 = Cesar(name, new_garages, register_id)
        self.assertNotEqual(cesar1, cesar2)


if __name__ == '__main__':
    unittest.main()
