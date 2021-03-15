from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} s to run.')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()
# SOME EXAMPLES OF DECORATORS : Log in, authentication, etc.