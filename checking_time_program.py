import datetime
import random

a = []
inf = 1e9
t0 = datetime.datetime.now()


def enter():
    for i in range(1, 100):
        a.append(random.randint(-inf, inf))


def _min():
    minn = inf
    for i in a:
        if (minn > i):
            minn = i
    print('MIN = ', minn)


def _max():
    maxx = -inf
    for i in a:
        if (maxx < i):
            maxx = i
    print('MAX = ', maxx)


def _sum():
    summ = 0
    for i in a:
        summ = summ + i
    print('SUM = ', summ)


def _mult():
    mult = 1
    for i in a:
        mult = mult * i
    print('MULTI = ', mult)


enter()
_min()
_max()
_sum()
_mult()
print(' ')
t1 = datetime.datetime.now() - t0
print(t1)
