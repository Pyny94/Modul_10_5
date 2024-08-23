import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'Линейный вызов: {linear_time}')

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f'Многопроцессный вызов: {multiprocess_time}')