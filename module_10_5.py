import multiprocessing
import datetime

def read_info(name):
    all_data = []
    file = open(name, 'r')
    line = file.readline().strip()
    while line:
        all_data.append(line)
        line = file.readline().strip()
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    t2 = datetime.datetime.now()
    print(f'{t2 - t1} (линейный)')

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        t3 = datetime.datetime.now()
        pool.map(read_info, filenames)
        pool.close()
        pool.join()
    t4 = datetime.datetime.now()
    print(f'{t4 - t3} (многопроцессный)')