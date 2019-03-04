# map ile bir listeyi bir fonksiyonun icine atıp yeni bi liste olusturabiliriz

def add(x):
    return x**2

array = [1, 2, 3, 4, 5]
print(list(map(add, array)))
# [1, 4, 9, 16, 25]
# lambda ile kullanımı

print(list(map(lambda x: x**2, array)))
# [1, 4, 9, 16, 25]
# map ile map objesi olusur objenin icini görebilmek icin list e type casting yaptik



