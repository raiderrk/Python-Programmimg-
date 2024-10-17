class Employee:
    
    
    def __init__(self):
        
      
    
        self.empId=101 #public
        self.empName='John' #public
        self.empDept='Dev'#public
        self.__empSal=50000 #private
        self.__printEmpDetails() 
        
        
    def __printEmpDetails(self): #private
        print("************Employee Object**************");
        print(self.empId)
        print(self.empName)
        print(self.empDept)
        print(self.__empSal)       
        
        
emp=Employee();
# emp.printEmpDetails()
# print(emp.empSal)



class ExtractEmployeesInfo:

      
      def extractInfo(self):
         print(".......Extract Info......")
         a=Employee();
         print(a.empId)
         print(a.empName)
         print(a.empDept)
          
ee=ExtractEmployeesInfo();
ee.extractInfo()          
        