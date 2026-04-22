import math
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
PRIMES=[112272535095293]*100

def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    sqrt_n=int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n%i==0:
            return False
    return True

def single_thread():
    for num in PRIMES:
        is_prime(num)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

if __name__ == '__main__':
    star=time.time()
    single_thread()
    end=time.time()
    print("single_thread time:",end-star,"seconds")

    star = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread time:", end - star, "seconds") #默认是cpu数量的线程数

    star = time.time()
    multi_process()
    end = time.time()
    print("multi_process time:", end - star, "seconds")
