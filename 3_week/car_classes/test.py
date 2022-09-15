from solution import *

car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
# car
# Bugatti Veyron
# bugatti.png
# 0.312
# 2

truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
# truck
# Nissan
# nissan.jpeg
# 3.92
# 2.09
# 1.87

spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
# spec_machine
# Komatsu-D355
# 93.0
# d355.jpg
# pipelayer specs

print(spec_machine.get_photo_file_ext())
#'.jpg'

cars = get_car_list('cars_week3.csv')
print(len(cars))
# 4

for car in cars:
    print(type(car))
# <class 'solution.Car'>
# <class 'solution.Truck'>
# <class 'solution.Truck'>
# <class 'solution.Car'>

print(cars[0].passenger_seats_count)
# 4

print(cars[1].get_body_volume())
# 60.0

cars_test = get_car_list('cars_invalid_only.csv')
print(cars_test)

cars_test = get_car_list('cars_valid_only.csv')
for car in cars_test:
    print(car)

car = Car('Bugatti Veyron', 'bugatti.pdf', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

truck = Truck('Nissan', 't1.jpg', '2.5', '')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')

car = Car('', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
