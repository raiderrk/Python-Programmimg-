class Employee:

    depart="developer"

    def empDepart(self):
        # self.depart=depart
        print(self.depart)
        # print(depart)

    @classmethod
    def empsal(cls):
        a=Employee
        a.sal=depart
        print(a.sal)
        # print(depart)
    # @staticmethod
    # def dsg(depart):
    #     print(depart)    

e=Employee()
e.empDepart()
e.empsal()
# e.dsg()


