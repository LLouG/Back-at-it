Lambdas = "https://youtu.be/HGOBQPFzWKo?t=6712"
#Lambda arguments: expression 

#add10 = lambda x: x + 10
#print(add10(5))
#mult = lambda x,y: x*y
#print(mult(2, 7))

#points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
#points2D_sorted = sorted(points2D, key=lambda x: x[1]) #sort elements according to the y index
#print(points2D)
#print(points2D_sorted)

#a = [1, 2, 3, 4, 5]
#b = map(lambda x: x*2, a) #multiply all elements by 2
#print(list(b))
#c = [x*2 for x in a] #Does the same thing as b
#print(c)

#a = [1, 2, 3, 4, 5, 6]
#b = filter(lambda x: x%2==0, a) #Return only the even numbers
#print(list(b))
#c = [x for x in a if x%2==0]
#print(c)

#from functools import reduce
#a = [1, 2, 3, 4]
#prod_a = reduce(lambda x,y: x*y, a)
#print(prod_a)


Exceptions = "https://youtu.be/HGOBQPFzWKo?t=7443"
#Errrors and Exceptions

#x = -5
#if x < 0:
#    raise Exception('x should be positive')

#y = -5
#assert (y>=0), 'x is not positive'

#try:
#    a = 5 / 0
#    b = a + '10'
#except ZeroDivisionError as f:
#    print(f)
#except TypeError as e:
#    print(e)
#else:
#    print("Everything is fine")
#finally:
#    print("Cleaning up...")

#class ValueTooHighError(Exception):
#    pass
#class ValueTooSmallError(Exception):
#    def __init__(self, message, value):
#        self.message = message
#        self.value = value
#def test_value(x):
#    if x > 100:
#        raise ValueTooHighError("Value is too high")
#    if x < 5:
#        raise ValueTooSmallError("Value is too small", x)
#try:
#    test_value(1)
#except ValueTooHighError as e:
#    print(e)
#except ValueTooSmallError as e:
#    print(e.message, e.value)


Logging = "https://youtu.be/HGOBQPFzWKo?t=8409"
#Logging: 

#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

#see helper.py
#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')
#import helper
#import logging
#logger = logging.getLogger(__name__)
#create handler
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('file.log')
#level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)
#formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)
#logger.addHandler(stream_h)
#logger.addHandler(file_h)
#logger.warning('this is a warning')
#logger.error('this is an error')

#import logging
#import logging.config
#logging.config.fileConfig('logging.conf')
#logger = logging.getLogger('simpleExample')
#logger.debug('this is a debug message')

#import logging
#import traceback
#try:
#    a = [1,2,3]
#    val = a[4]
#except:
#    logging.error("The error is %s", traceback.format_exc())

#import logging
#from logging.handlers import RotatingFileHandler
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
## roll over after 2KB and keep backup logs app.log.1, app.log.2 , etc.
#handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
#logger.addHandler(handler)
#for _ in range(10000):
#    logger.info('Hello, world!')

#import logging
#from time import sleep
#from logging.handlers import TimedRotatingFileHandler
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
# s, m, h, d, midnight, w0
#handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
#logger.addHandler(handler)
#for _ in range(6):
#    logger.info('Hello, world!')
#    sleep(5)