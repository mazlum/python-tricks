from dataclasses import dataclass
#Python 3.7 ve üst sürümlerde de geçerlidir.
# :str veya -> str gibi göreceğiniz syntax bilgilendirme(dökümantasyon) amaçlıdır.
# Değişken veya fonksiyon için validation özelliği taşımaz.

#namedtuple ile yaptığımız işlemi Class lar ile yapabiliriz dersek aşağıdaki işlemi uygulamalıyız.

class DataClassExmp:
    def __init__(self,name:str, last_name:str, phone: int):
        self.name = name
        self.last_name = last_name
        self.phone = phone

#Buradaki verilere ulaşmak için:
classexmp = DataClassExmp(name='mesut', last_name='oncel', phone=10)
print(f'--> standart class ==> {classexmp.name}')

#OUTPUT:
# --> standart class ==> mesut

#Bu işlemi dataclass ile yapmak istersek:

@dataclass
class Exmp:
    name: str 
    last_name : str 
    phone_number : int

exmp = Exmp(name='mesut', last_name='oncel', phone_number=123123)
print(f'--> dataclass ==> {exmp.name}, {exmp.last_name}, {exmp.phone_number}')
#OUTPUT:
# --> dataclass ==> mesut, oncel, 123123

# DataClassExmp i yazdırmak istersek "<__main__.DataClassExmp object at 0x102786e80>" çıkacaktır.
# Exmp (dataclass özelliği taşıyan) class direk print ettiğimizde 
# Exmp(name='mesut', last_name='oncel', phone_number=123123) çıktısını alacağız


#Dataclass ait field lara default değer verebilirsiniz.
@dataclass
class ExmpDefault:
    name: str 
    last_name : str = None
    phone_number : int = +90123123

exmp = ExmpDefault(name='mesut')
print(f'--> dataclass default ==> {exmp.name}, {exmp.last_name}, {exmp.phone_number}')

#OUTPUT:
# dataclass default ==> mesut, None, 90123123

# namedtupler lar doğası gereği değiştirilmezdir. 
# Yani bir namedtuple a ait bir field ın değeri "doğrudan" değiştirilemez.
# Ancak dataclasslar ile parametrelerde değişiklik yapabiliriz.

exmp.last_name = 'xxx'
print(f'--> güncellenmiş dataclass ==> {exmp.name}, {exmp.last_name}, {exmp.phone_number}')
#OUTPUT:
# --> güncellenmiş dataclass ==> mesut, xxx, 123123

#Immutable özelliği vermek için

@dataclass(frozen=True)
class FrozenData:
    name:str
frozen_exmp = FrozenData(name='mesut')
frozen_exmp.name = 'ahmet'

#OUTPUT

"""
Traceback (most recent call last):
  File "dataclass.py", line 62, in <module>
    frozen_exmp.name = 'ahmet'
  File "<string>", line 3, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'name'
"""

#istediğimiz veriyi modifiye ederek kullanıcıya bir method sunabiliriz.

@dataclass
class ExmpTwo:
    name: str 
    last_name : str
    phone_number : int

    @property   
    def international_code(self)-> str:
        return f'+00{self.phone_number}'

exmp_two = ExmpTwo(name='mesut', last_name='oncel', phone_number=123123)
print(f'--> fonksiyon çıktısı : {exmp_two.international_code}')
#OUTPUT:
# --> fonksiyon çıktısı : +00123123

#Class  oluşturmadan dataclass oluşturabiliriz.
from dataclasses import make_dataclass

makedataclass = make_dataclass('MakeDataClass', ['name', 'last_name', 'phone'])
makedataclass_ = makedataclass('mesut', 'oncel', '+901323')
print(makedataclass_)
#OUTPUT:
# MakeDataClass(name='mesut', last_name='oncel', phone='+901323')

#Inheritance

@dataclass
class NewData(ExmpTwo):
    pass

newdata = NewData(name='mesut',last_name='oncel', phone_number=1232)
print(newdata)

#OUTPUT:
# NewData(name='mesut', last_name='oncel', phone_number=1232)
