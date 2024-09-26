from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)
        self.power = int(power)
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали!')
        day_battle = 0
        janki = 100
        while janki > 0:
            day_battle +=1
            janki -= self.power
            sleep(1)
            print(f'{self.name_} сражается {day_battle}-й день..., осталось '
                  f'{janki} воинов.')
        print(f'{self.name_} одержал победу спустя {day_battle} дней(дня)!')

threads = []

first_knight = Knight('Dobrynya Nikitich', 10)
second_knight = Knight("Ilya Muromets", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
