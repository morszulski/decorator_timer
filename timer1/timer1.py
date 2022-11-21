import sys
import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        print('Function took:', time.time() - before, 'seconds')
        return val

    return wrapper


@timer
def main(seconds=0):
    time.sleep(seconds)
    return None


if __name__ == '__main__':
    sys.exit(main(.91))
