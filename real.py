import math

class Real:
    def __init__(self, witdth, height):
        self.width = witdth
        self.height = height

    def __str__(self):
        return f"{self.diognal:.2f} cm"
    

    @property
    def diognal(self):
        self._diognal = math.sqrt(self.width ** 2 + self.height ** 2)
        return self._diognal
    
    
    @diognal.setter
    def diognal(self, diognal):
        self._diognal = diognal

    

real = Real(16, 9)
print(real)