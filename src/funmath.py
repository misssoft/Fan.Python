import sys
from math import factorial
from math import sqrt

def calculateFactorial(num):
    x = range(0, num)
    f = [factorial(x) for x in range(num)]
    l = [len(str(factorial(x))) for x in range(num)]

    for i in range(num):
        print({i},"-", {f[i]}, "-", {l[i]} )

def calculateFactorialinloop(num):
    for i in range(num):
        print({i}, "=", factorial(i), "=", len(str(factorial(i))))

def calculateFibonacci(num):
    if num>1:
        sum = calculateFibonacci(num - 2) + calculateFibonacci(num -1)
        print('fab(',{num},') = ',{sum})
        return sum
    print('fab(',{num},') = ',{num})
    return num

def calculateFiboFaster(num):
    if (num>=1):
        a, b = 0,1
        counter = 0
        while counter < num:
            counter = counter + 1
            a,b = b, a+b
            print('fab(',counter,') = ',{b})
    a,b = 0,0
    
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    print(x)
    return True


def printPrime(num):
    y = [x for x in range(num) if isPrime(x)]
    for item in y:
        print(item)


def main(x):
    try:
        #calculateFactorial(x)
        #calculateFactorialinloop((x))
        #calculateFibonacci(x)
        calculateFiboFaster(x)
        #printPrime(x)
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Continues")

if __name__ == '__main__':
    main(sys.argv[1])