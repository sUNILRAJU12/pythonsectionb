from abc import ABC, abstractmethod
class modelcar(ABC):
    @ abstractmethod
    def Break():                    
        pass                    
    @abstractmethod
    def speed_up():
        pass
class x6 (modelcar):
    def __init__ (self,speed=0,stop=True):
        self.speed = speed
        self.stpo = stop
    def speed_up(self):
        self.speed=5
        self.stop = True
    def Break(self):
        print(f'accelarated by 5 km/hr and current speed is {self.speed}')
obj = x6


