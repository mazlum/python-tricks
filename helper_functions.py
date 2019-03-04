from functools import reduce

array = [1, 2, 3, 4, 5]
# map ile bir listeyi bir fonksiyonun icine atıp yeni bi liste olusturabiliriz

def add(x):
    return x**2

print(list(map(add, array)))
# [1, 4, 9, 16, 25]

# lambda ile kullanımı
print(list(map(lambda x: x**2, array)))
# [1, 4, 9, 16, 25]


#filter yardimci fonksiyonu verdigimiz kurala uygun olan elemanlari bir list icinde dondurur

print(list(filter(lambda x: x<3, array)))
# [1, 2]

# reduce fonksiyonunda lambda iki parametre alir. ilk önce listenin ilk iki parametresini alip bir deger dondurur ardından dondurdugu deger ile listenin 3. elemanını alır ve bir deger dondurur. bu sekilde son bir sonuc cıkana kadar devam eder. reduce list degil bir deger dondurur

print(reduce((lambda x, y: x+y), array))
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# sonuc = 15

 

# map ve filter bize obje dondurur, objenin tasidigi degeri gorebilmek icin type cast ile list tipine ceviriyoruz
