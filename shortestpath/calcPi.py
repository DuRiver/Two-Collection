import math
import decimal

def calcPi(n):

    re = 3
    decimal.Decimal(re)
    if(n == 1):
        print(re)
    elif(n > 1):
        for i in range(1, n + 1):
            k = 2 * i
            sign = math.pow(-1, i+1)
            re += sign * 4 / (k * (k + 1) * (k + 2))
        print(re)
    else:
        return "wrong!"


if __name__ == '__main__':
    calcPi(10000000)
