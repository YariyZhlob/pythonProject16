class StartCar:
    def turn_key(self):
        print('Turn the key ON')

    def __turn_starter(self):
        print('starter motor is swithced ON')

    def __switch_fuel_valve(self):
        print('fuel valve is switched ON')

    def _switch_door_blocker(self):
        print('doors are blocked')

start = StartCar()
start.turn_key()
start._switch_door_blocker()

a = 90 +3j
print(type(a))
s = float('inf')
print(type(s))
x = False + False + False + True
print(x)