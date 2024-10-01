import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            if not line:
                break
            else:
                all_data.append(file.readline())

if __name__ == '__main__':
    start = datetime.now()
    for i in range(1, 5):
        read_info(f'file {i}.txt')
    end = datetime.now()
    print(end - start, '(линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        all_file = []
        for i in range(1, 5):
            all_file.append(f'file {i}.txt')
        start = datetime.now()
        pool.map(read_info, all_file)
    end = datetime.now()
    print(end - start, '(многопроцессный)')

