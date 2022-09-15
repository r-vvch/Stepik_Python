import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if not (brand and photo_file_name and carrying and
                os.path.splitext(photo_file_name)[1] in ['.jpg', '.jpeg', '.png', '.gif']):
            raise ValueError
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        if not passenger_seats_count:
            raise ValueError
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        try:
            body_length, body_width, body_height = map(float, body_whl.split('x'))
        except (TypeError, ValueError):
            body_length = body_width = body_height = 0.0
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        if not extra:
            raise ValueError
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                if car_type == 'car':
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine':
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except (ValueError, IndexError):
                pass
    return car_list
