from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Test(Base):
    def foo(self):
        pass


assert issubclass(Test, Base)
# https://docs.python.org/3/library/abc.html
