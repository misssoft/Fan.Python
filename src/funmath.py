import sys
from math import factorial

def calculateFactorial(num):
    x = range(0, num)
    f = [factorial(x) for x in range(num)]
    l = [len(str(factorial(x))) for x in range(num)]

    for i in range(num):
        print({i},"-", {f[i]}, "-", {l[i]} )

def main(x):
    try:
        calculateFactorial((x))
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Continues")

if __name__ == '__main__':
    main(sys.argv[1])