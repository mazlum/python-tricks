import functools


def lowercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().lower()

    return wrapper


@lowercase
def lower():
    """Say hello"""
    return "Hello world!"


print(lower.__name__)
print(lower.__doc__)
# functiontools kullanarak  =>
"""
lower
Say hello
"""

# functools kullanmadan (Burada kullandığımız fonksiyon wrapper fonksiyonu oluyor.) =>
"""
wrapper
None
"""

# use decorators with arguments
def decorator_with_arguments(arg1):
    def real_decorator(func):
        @functools.wraps(func)
        def runs_func(*args, **kwargs):
            print("Decorator starts")
            if isinstance(arg1, int):
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("It's over")

        return runs_func

    return real_decorator


# use decorator
@decorator_with_arguments(1)
def f1(x, y):
    print("example")


@decorator_with_arguments("arg")
def f2(x, y):
    print(x + y)


f1()
"""
Decorator starts
Not running the function
It's over
"""
f2(10, 20)
"""
Decorator starts
30
It's over
"""
