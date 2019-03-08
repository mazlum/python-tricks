from collections import namedtuple

Book = namedtuple('Book', ['name', 'page'])

our_book = Book('Python', 218)
# namedtuple ile doğrudan property şeklinde erişim sağlayabiliyoruz.
print(our_book.name)
print(our_book._fields)
"""Çıktı
Python
('name', 'page')
"""

# namedtuple methodları
# _asdict
our_book._asdict()
# _replace
# Replace methodu var olanı değiştirmez. 
# namedtuple'de regular tuple gibi immutable olduğu 
# için shallow copy ile yeni bir nesne oluşturur.
our_book2 = our_book._replace(page=20)
print(our_book)
print(our_book2)
"""Çıktı
Book(name='Python', page=218)
Book(name='Python', page=20)
"""

# _make doğrudan bir nesne oluşturmamızı sağlar.
our_book3 = Book._make(['Django', 432])
print(our_book3)
