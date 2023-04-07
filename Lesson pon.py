import time
def timeit(func):#Ця функція використовує модуль time, щоб виміряти час виконання функції func.
# Після виконання вхідної функції func вона виводить час виконання у консоль за допомогою функції print та повертає результат виконання функції.
    def wrapper(args, **kwargs):
        start_time = time.time()
        result = func(args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

#Для перевірки працездатності функції timeit можна написати тестові функції з відповідними вхідними даними та очікуваними результатами.
#Наприклад:
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