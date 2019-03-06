import copy
# Deep copy
l1 = [1, 2, [1, 2], [1, 1]]
# l1'den yeni bir liste oluşturma;
l2 = l1.copy()
# Bu yöntemde liste içindeki liste elemanları kopyalanmaz. Yani referansları aynı kalır.
l1.append(4)
print("l1 => ", l1)
print("l2 => ", l2)
"""Çıktı
l1 =>  [1, 2, [1, 2], [1, 1], 4]
l2 =>  [1, 2, [1, 2], [1, 1]]
"""
l1[2].append(10)
print("l1 => ", l1)
print("l2 => ", l2)
"""Çıktı
Her iki liste içinde içerideki listeye eleman eklenmiş oldu.
l1 =>  [1, 2, [1, 2, 10], [1, 1], 4]
l2 =>  [1, 2, [1, 2, 10], [1, 1]]
"""
z1 = [1, 2, [1, 2]]
z2 = copy.deepcopy(z1)
z1[2].append(3)
print(z1)
print(z2)
"""Çıktı
[1, 2, [1, 2, 3]]
[1, 2, [1, 2]]
"""

# Listeyi ters çevirme 
print('Ters l1 =>', l1[::-1])  # Ters l1 => [4, [1, 1], [1, 2, 10], 2, 1]

print('Ters l2 =>', list(reversed(l2)))  # Ters l2 => [[1, 1], [1, 2, 10], 2, 1]