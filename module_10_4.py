from threading import Thread
import queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number, guest = None):
        self.number = int(number)
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        free_tables = len(self.tables)
        for guest in guests:
            if not free_tables:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер'
                          f' {table.number}')
                    break
            free_tables -= 1

    def discuss_guests(self):
        while any(table.guest is not None for table in
                  self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest.join()
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(
                                f'{table.guest.name} вышел(-ла) из очереди '
                                f'и сел(-а) за стол номер {table.number}')
                        else:
                            table.guest = None


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

