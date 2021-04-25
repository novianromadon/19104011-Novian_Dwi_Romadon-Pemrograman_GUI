from abc import ABCMeta,abstractmethod
# kelas abstract
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

# Kelas segiEmpat turunan dari kelas duaDimensi
class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
# implementasi metode luas()
    def luas(self):
        return self.panjang * self.lebar

# Kelas Segitiga turunan dari kelas DuaDimensi