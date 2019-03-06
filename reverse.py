py = 'pythontricks'
py_num = 1234567


print(py[::-1])
print(str(py_num)[::-1])


for i in reversed(py):
    print(i, end='')
    """
    end parametresi kullanmazsak çıktımız şu şekilde olur
    s
    k
    c
    i
    r
    t
    n
    o
    h
    t
    y
    p
    """


for k in reversed(str(py_num)):
    print(k, end='')


