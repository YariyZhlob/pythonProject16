class Car:
    def car_description(self, brand, power, max_speed):
        return f'information about car: brand is {brand}, power is {power}, maximum speed is {max_speed}'

audi = Car().car_description('Audi', 250, 300)
bmw = Car().car_description('BMW', 200,200)
mercedes = Car().car_description('Mercedes-Benz', 180, 240)
print(audi, bmw, mercedes, sep= '\n')