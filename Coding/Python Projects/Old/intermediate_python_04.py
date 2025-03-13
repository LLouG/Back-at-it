Random_Numbers = "https://youtu.be/HGOBQPFzWKo?t=10783"

#import random
#random.seed(1) #not recommended for security reasons
#print(random.random())
#print(random.randint(1, 10))
#random.seed(2312312)
#print(random.random())
#print(random.randint(1, 10))

#import secrets
#a = secrets.randbelow(10)
#b = secrets.randbits(4)
#mylist = list("ABCDEFGH")
#d = secrets.choice(mylist)
#print(a)
#print(b)
#print(d)

#import numpy as np
#a = np.random.randint(0, 10, (3,4))
#print(a)
#np.random.seed(1)
#print(np.random.rand(3,3))
#np.random.seed(2)
#print(np.random.rand(3,3))


Decorators = "https://youtu.be/HGOBQPFzWKo?t=11665"

#import functools
#def repeat(num_times):
#    def decorator_repeat(func):
#        @functools.wraps(func)
#        def wrapper(*args, **kwargs):
#            for _ in range(num_times):
#                result = func(*args, *kwargs)
#            return result
#        return wrapper
#    return decorator_repeat
#@repeat(num_times=3)
#def greet(name):
#    print(f'Hello {name}')
#greet('Loug')

#import functools
#def start_end_decorator(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        print('Start')
#        result = func(*args, **kwargs)
#        print('End')
#        return(result)
#    return wrapper
#def debug(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        args_repr = [repr(a) for a in args]
#        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
#        signature = ", ".join(args_repr + kwargs_repr)
#        print(f"Calling {func.__name__} ({signature})")
#        result = func(*args, **kwargs)
#        print(f"{func.__name__!r} returned {result!r}")
#        return result
#    return wrapper
#@debug
#@start_end_decorator
#def say_hello(name):
#    greeting = f'Hello {name}'
#    print(greeting)
#    return greeting
#say_hello("Loug")


Generators = "https://youtu.be/HGOBQPFzWKo?t=12932"
#Generators: more memory efficient

#def mygenerator():
#    yield 1
#    yield 2
#    yield 3
#g = mygenerator()
#value = next(g)
#print(value)
#value = next(g)
#print(value)

#def countdown(num):
#    print('Starting')
#    while num > 0:
#        yield num
#        num -= 1
#cd = countdown(4)
#value = next(cd)
#print(value)
#print(next(cd))
#print(next(cd))
#print(next(cd))

#import sys
#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums
#def firstn_generator(n):
#    num = 0
#    while num < n:
#        yield num
#        num += 1
#print(sys.getsizeof(firstn(1000000)))
#print(sys.getsizeof(firstn_generator(1000000)))

#def fibonacci(limit):
#    # 0 1 1 2 3 5 8 13 ... sum of previous numbers
#    a, b = 0, 1
#    while a < limit:
#        yield a
#        a, b = b, a + b
#fib = fibonacci(30)
#for i in fib:
#    print(i)

Threading_vs_Multiprocessing = "https://youtu.be/HGOBQPFzWKo?t=14010"


Threading = "https://youtu.be/HGOBQPFzWKo?t=14881"

#from threading import Thread, Lock, current_thread
#from queue import Queue
#def worker(q, lock):
#    while True:
#        value = q.get()
#        with lock:
#            print("in {} got {}".format(current_thread().name, value))
#        q.task_done()
#if __name__ == "__main__":
#    q = Queue()
#    lock = Lock()
#    num_threads = 4
#    for i in range(num_threads):
#        thread = Thread(target=worker, args=(q, lock))
#        thread.daemon=True
#        thread.start()
#    for i in range(1, 21):
#        q.put(i)
#    q.join()
#    print('end main')


Multiprocessing = "https://youtu.be/HGOBQPFzWKo?t=16266"

#from multiprocessing import Process, Array, Lock
#from multiprocessing import Queue
#import time
#def add_100(numbers, lock):
#    for i in range(100):
#        time.sleep(0.01)
#        for i in range(len(numbers)):
#            with lock:
#                numbers[i] += 1
#if __name__ == "__main__":
#    lock = Lock()
#    shared_array = Array('d', [0.0, 100.0, 200.0])
#    print('Array at beginning is', shared_array[:])
#    p1 = Process(target=add_100, args=(shared_array, lock))
#    p2 = Process(target=add_100, args=(shared_array, lock))
#    p1.start()
#    p2.start()
#    p1.join()
#    p2.join()
#    print('Array at end is', shared_array[:])

#from multiprocessing import Pool
#def cube(number):
#    return number * number * number
#if __name__ == "__main__":
#    numbers = range(10)
#    pool = Pool()
#    result = pool.map(cube, numbers)
#    pool.close()
#    pool.join()
#    print(result)
