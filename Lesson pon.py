import time
def timeit(func):
    def wrapper(args, **kwargs):
        start_time = time.time()
        result = func(args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper
def test_factorial():
    @timeit
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120