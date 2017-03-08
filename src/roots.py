import sys

def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria
    Args:
        x: The number for which the square root is to be computed.
    Returns:
        The square root of x.
    '''
    if x<0:
        raise ValueError("Cannot compute square root of a negative number.")
    guess = x
    i=0
    while guess * guess != x and i<20:
        guess = (guess + x/guess) / 2.0
        i+=1
    return guess

def main(x):
    try:
        print(sqrt(x))
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Continues")

if __name__ == '__main__':
    main(sys.argv[1])
