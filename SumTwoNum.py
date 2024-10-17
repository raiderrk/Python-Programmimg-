

# def sum(num,num1):

#     sum=num+num1;
#     return (f'sum of two no is: {sum}')

# num =int(input('first no: '))
# num1 =int(input("second no: "))

# s=sum(num,num1)
# print(s)


# *******************find the number prime and odd number  If prime return True else Odd Return 

# num = int(input('enter : '));

# def Is_even(num):

#     if (num%2==0):
      
#       return True
    
#     else:
#        return False
    
# i=Is_even(num)    
# print(i)


#*********************Even OR Odd *******************#


# num = int(input())

# def Is_odd(num):

#     if (num//2==0):

#         return False
#     else:

#         return True
    
# ii=Is_odd(num)
# print(ii)    



# *********Using List***********


# n = int(input())

# l=['even','odd']
# print (l[n%2])



# ************* find the number -ve or +ve ************


# num = int(input("enter the number:  "))

# def Is_pve_nve(num):

#     if num>0:
#         return "positive"
    
#     elif num<0:

#         return "negative"
    
#     else:

#         return "zero"
    

# p=Is_pve_nve(num)

# print(p)




# class invalidAgeEception(BaseException):
#     def __init__(self):
#         message="age is below 18"
#         super().__init__(message);


# class Vote:
#     def checkAge(self,age ):
#         self.age = age;

#         if self.age >=18:
#             print("You are  eligible  for vote")

#         else:
#             raise invalidAgeEception() 


# v=Vote()
# try:
#     v.checkAge(19)
# except invalidAgeEception:
#     print("Only 18 and above people allow to vote")




# from abc import ABC,abstractclassmethod

# class Db(ABC):

#     @abstractclassmethod
#     def connect(self):
#         pass;

#     def insertData(self):
#         print('Inserting The Data');

# class Mysql(Db):

#     def connect(self):
#         print("Connection Established in Mysql Successfully ")



# m=Mysql()

# m.insertData()
# m.connect()

# class Employee:

#     def __init__(self):
    
#         self.__empid=None;
#         self.__name=None;
#         self.__empsal=None;
 
#     def getId(self):
#         return self.__empid;

#     def setId(self,empid):
#         self.__empid=empid;

#     def getName(self):
#         return self.__name;

#     def setName(self,name):
#         self.__name=name;

#     def getSal(self):
#         return self.__empsal;

#     def setSal(self,empsal):
#         self.__empsal=empsal;


#     def displayDetails(self):
#         print(e.getId())
#         print(e.getName())
#         print(e.getSal())


# e=Employee()
# e.setId(101)
# e.getId()
# e.setName("Rahul")
# e.getName()
# e.setSal(100000)
# e.getSal()
# e.displayDetails()




l={1,2,3,4,5,6}
l1={7,8,9,10,6,4}


print(type(l))

# print(l.remove(2))
print(l)
l.add(40)
print(l)
l.discard(4)
print(l)
l.update(l1)
print(l)

s1=l.union(l1)
print(s1)

s2=l.intersection(l1)
print(s2)

s3=l.difference(l1)
print(s3)

s4=l.symmetric_difference(l1)
print(s4)



t=(1,2,3,4,5,6,4,4,4,4,4)

print(type(t))
print(t)
p=t.index(4)
print(p)
c=t.count(4)
print(c)

s="tree"
print(type(s))
j=s.join("e")
print(j)
print(s)

dict=  {
    'e':"one",
    1:'k',
    3:'b',
    5:6,}

   

print(type(dict))
k=dict.keys()
print(k)
t=dict.values()
print(t) 


        










