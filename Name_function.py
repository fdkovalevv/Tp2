f = [int(i) for i in (open('10.txt').readlines())[0].split(' ')[:-1]]
def _min(f):
    minn = 100000
    for i in f:
        if minn > i:
            minn = i
    return minn
print('Минимальное:', _min(f))
def _max(f):
    maxx = -10^20
    for i in f:
        if maxx < i:
            maxx = i
    return maxx
print('Максимальное:', _max(f))
def _sum(f):
    summ = 0
    for i in f:
        summ += i
    return summ
print('Сумма:', _sum(f))
def _mult(f):
    mult = 1
    for i in f:
        mult *= i
    return mult
print('Произведение:', _mult(f))

def _pop(f):
    _p = 0
    for i in f:
        _p += i**2
    return _p
print('Сумма квдратов:', _pop(f))
