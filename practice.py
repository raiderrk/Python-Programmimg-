
class Teacher:
    name="vivek"

     
    def deatils(self,name):
        
        self.name=name
        print(self.name);
        
    @classmethod 
    def work(cls):
            
        print("Rahul")
     
     #   a=Teacher()
        a=Teacher.name
        print(a);
            
    @staticmethod 
    def teches():
        print("static")
      #  a1=Teacher()
        a1=Teacher.name
        print(a1);
            
            
t=Teacher()
t.deatils("nm");   
t.work()
t.teches()
    
            
        
    