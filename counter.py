# collections kütüphanesi kullanarak
from collections import Counter

list_ = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 5]
print(Counter(list_))

# Counter kullanmadan
count = {}
for i in list_:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1
print(count)