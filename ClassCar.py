class Car:
    def __init__(self, model, production_year, motor_volume, price, distance):
        self.model = model
        self.production_year = production_year
        self.motor_volume = motor_volume
        self.price = price
        self.distance = distance
        self.wheels = 4

    def car_description(self):
        return "Алекс, твой новый автомобиль- " + f"модель {self.model}, c {self.wheels} колесами, " + f"год производства {self.production_year}, " + f"с объемом двигателя {self.motor_volume} литра, " + f"купленный за {self.price} рублей, " + f"с пробегом {self.distance} километров"

    def change_wheels_number(self, wheels_number):
        self.wheels = wheels_number


alex_car = Car('Audi', 2023, 2.5, 40000, 10)
print(alex_car.car_description())


class Truck(Car):
    def __init__(self, model, production_year, motor_volume, price, distance):
        super().__init__(model, production_year, motor_volume, price, distance)


volvo_truck = Truck("Volvo", 2023, 4, 50000, 10000)
volvo_truck.change_wheels_number(8)
print(volvo_truck.car_description())
