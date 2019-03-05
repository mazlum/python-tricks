# tek satirda if ile deger atama
# (atanacak deger) if (kosul) else (kosul saglanmazsa atanacak deger)

deger = 'Python' if 10<11 else 'Ruby'
print(deger)
# Python

# tek satirda for ile list olusturma
# [ (listeye eklenecek degisken) for (for ile gelen data) in (for ile dolaşılan data) ]

data = [1, 2, 3, 4, 5]
array = [ x+2 for x in data ]
print(array)
# [3, 4, 5, 6, 7]

# eger istenirse if ile de kullanılabilir

array = [ x+2 for x in data if x<3 ]
print(array)
# [3, 4]

