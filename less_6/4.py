
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def go(self):
        print('{} is stoping!'.format(self.name))

    def go(self, direction):
        print('{} is turning to'.format(self.name, direction))

    def show_speed(self):
        print('Current speed', self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60
            print('Speed is more then max!')

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print('Current speed:' self.speed)
        if self.speed > 40:
            return ('Speed is more then max!')
class PoliceCar(Car):
    pass


