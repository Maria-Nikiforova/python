class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('ручка рисует')

class Pencil(Stationery):
    def draw(self):
        print('карандаш рисует')


class Hendle(Stationery):
    def draw(self):
        print('маркер рисует')

pen = Pen('ручка')
pencil = Pencil ('карандаш')
hendle = Hendle('маркер')

