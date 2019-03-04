import random

months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#yield kullanarak

def random_month_yield(max_len=10):
    for i in range(1,max_len+1):
        yield {i: random.choice(months)}

print(list(random_month_yield()))

#Output
"""
 [{1: 'Jul'},
 {2: 'May'},
 {3: 'Jun'},
 {4: 'Dec'},
 {5: 'Nov'},
 {6: 'Jun'},
 {7: 'May'},
 {8: 'Sep'},
 {9: 'Jan'},
 {10: 'Dec'}]

 """

#yield kullanmadan 
def random_month(max_len=10):
    data = []
    for i in range(1, max_len+1):
        item = {i: random.choice(months)}
        data.append(item)
    return data

print(random_month())
"""
[{1: 'Apr'},
 {2: 'Jan'},
 {3: 'Feb'},
 {4: 'Aug'},
 {5: 'Mar'},
 {6: 'May'},
 {7: 'Aug'},
 {8: 'Oct'},
 {9: 'Jun'},
 {10: 'May'}]
"""