import time
from multiprocessing import Pool


def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:
        while True:
            line = file.readline()  # Считываем строку из файла
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line)  # Добавляем строку в список


filenames = [f'./file{number}.txt' for number in range(1, 5)]

# # Линейный вызов
# start_time = time.perf_counter()
#
# for filename in filenames:
#     read_info(filename)
#
# end_time = time.perf_counter()
# print(f'Линейный вызов занял {end_time - start_time:.6f} секунд')

# Многопроцессный вызов
if __name__ == '__main__':
    start_time = time.perf_counter()

    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time = time.perf_counter()
    print(f'Многопроцессный вызов занял {end_time - start_time:.6f} секунд')
