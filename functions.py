# Bir fonksiyon hiç bir şey döndürmüyor ise Python otomatik olarak None döndürür.
def foo(value):
    if value:
        return value


print(foo(0))
# None
