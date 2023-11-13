from threading import Thread
import time
import math


def number(num):
    result = 0
    for i in range(num):
        result += math.sin(i)
        time.sleep(0.15)
        print(result)


def text(num):
    for i in range(num):
        print("OK")
        time.sleep(0.15)


thr_1 = Thread(target=number, args=(10,))
thr_2 = Thread(target=text, args=(10,))
thr_3 = Thread(target=text, args=(10,))

thr_1.start()
thr_2.start()
thr_3.start()


thr_1.join()
thr_2.join()
thr_3.join()

print("IJIJOIJOLIJOOIJOIJ")









