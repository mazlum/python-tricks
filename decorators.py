import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().lower()
    return wrapper


@uppercase
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
