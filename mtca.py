class mtca:
    principal='mr.prabhakar Naidu'
    college='MTCA'
    location='palamaneru'

    def __init__(self,name,mobile,email,sem):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.sem = sem

    def update_mob(self,new):
        self.mobile =new
        print('mobile number updated')

        @classmethod
        def change_principle(cls,new):
            cls,principle=new

