import sys

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter +=1
        yield item


def run_take(m,n):
    items = range(0,m)
    for item in take(n, items):
        print(item)


def main(x, y):
    try:
        run_take(x, y)
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Continues")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])