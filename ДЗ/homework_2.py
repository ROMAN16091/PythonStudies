

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
#
#
# print(is_prime(5))
# print(is_prime(6))

def find_primes_single_thread(start, end):
    simple_nums = []
    start = max(2, start)
    for i in range(start, end + 1):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            simple_nums.append(i)
    return simple_nums





import threading
import time

def find_primes_multi_thread(start, end):
    primes_part1 = []
    primes_part2 = []
    middle = (start + end) // 2
    def find_part1():
        for i in range(start, middle):
            if i > 1 and all( i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
                primes_part1.append(i)
    def find_part2():
        for i in range(middle + 1, end + 1):
            if i > 1 and all( i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
                primes_part2.append(i)
    thread_1 = threading.Thread(target=find_part1)
    thread_2 = threading.Thread(target=find_part2)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    return primes_part1 + primes_part2

start1 = time.time()
find_primes_single_thread(1, 100)
print(f'Функція з одним потоком з малим діапазоном: {(time.time() - start1) * 1000}')

start2 = time.time()
find_primes_multi_thread(1, 100)
print(f'Функція з мультипоточністю з малим діапазоном: {(time.time() - start2) * 1000}')

start3 = time.time()
find_primes_single_thread(1, 250000)
print(f'Функція з одним потоком з великиим діапазоном: {(time.time() - start3) * 1000}')

start4 = time.time()
find_primes_multi_thread(1, 250000)
print(f'Функція з мультипоточністю з великиим діапазоном: {(time.time() - start4) * 1000}')

# Для малих діапазонів багатопоточність не є ефективною через витрати на створення
# та управління потоками, які перевищують вигоду від паралельної обробки. В таких випадках однопотоковий підхід буде
# швидшим, оскільки час виконання обчислень є дуже малим. Для більш великих задач та діапазонів багатопоточність
# дає значну вигоду, оскільки дозволяє паралельно обробляти великі обсяги даних, що зазвичай зменшує загальний час.








