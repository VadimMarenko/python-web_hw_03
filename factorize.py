from multiprocessing import cpu_count, Pool
from time import time, sleep
import logging


def factorize(*number):
    result = []
    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_multi_proc(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    timer1 = time()
    factorize(*numbers)
    logging.info(f"\nThe process is complete in {time() - timer1}s\n")

    sleep(3)

    timer2 = time()
    num_cores = cpu_count()

    # pool = Pool(processes=num_cores)
    # factors_list = pool.map(factorize_multi_proc, numbers)
    # pool.close()
    # pool.join()
    # logging.info(f"{factors_list} \nMultiprocess time: {time() - timer2}s")

    with Pool(processes=num_cores) as pool:
        logging.debug(pool.map(factorize_multi_proc, numbers))
    logging.info(f"\nMultiprocess time: {time() - timer2}s")

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [
    1,
    2,
    4,
    5,
    7,
    10,
    14,
    20,
    28,
    35,
    70,
    140,
    76079,
    152158,
    304316,
    380395,
    532553,
    760790,
    1065106,
    1521580,
    2130212,
    2662765,
    5325530,
    10651060,
]
