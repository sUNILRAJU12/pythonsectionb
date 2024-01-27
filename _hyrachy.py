class MTCA:
    chairman ='mr. sunil '
    location = 'palamaneru'
    college = 'MTCA'

    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile

class MCA(MTCA):
    principal = 'mr. prabhakar naidu'
    strength  = 240
    staff     =9
    
class Btech(MTCA):
        principal ='chintu '
        strength  = 350
        staf      =35

Navyasree = MCA('navyasree',6305658968)
Rajashekar = Btech('Rajashekar',9492549295) 
