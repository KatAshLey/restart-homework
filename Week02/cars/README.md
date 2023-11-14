Given this example, customize the behavior of drive:
Inside ElectricCar class
redefine the `drive(self, distance)` function again
it will have same behavior regarding `milage_km`
but add in at the end some code so that the `self.range` gets subtracted by the drive `distance`
Test the drive behavior of ElectricCar class
initialize an object from ElectricCar class `my_ev`
call `my_ev.drive(some_distance)` a few times
notice via `print(my_ev.__dict__)` that the `range` has been reduced
Inside IceCar class
redefine the `drive(self, distance)` function again
it will have same behavior regarding `milage_km`
but add in at the end some code so that the `self.fuel_level` gets subtracted by the drive `distance*fuel_consumption/100` (how much fuel we will consume)
Test the drive behavior of IceCar class
initialize an object from ElectricCar class `my_ice_car`
call `my_ice_car.drive(some_distance)` a few times
notice via `print(my_ice_car.__dict__)` that the `fuel_level` has been reduced