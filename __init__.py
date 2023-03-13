#Types of variables:=1]Instance variable
#                    2] static variable/class variable
#                    3] local variable

# 1] Instance variable:- this variable can be chage object to object
# ========================
# here e1 & e2 these are two object
# when we need specific data then according to this object we will call this. e.g.:- e1.first,e2.id etc...

class Emp:
    def __init__(self,first,last,mob,mail,id):
        self.first = first
        self.last = last
        self.mob = mob
        self.mail = mail
        self.id = id

    def display(self):
        print('first::',self.first)
        print('last::',self.last)
        print('mob::',self.mob)
        print('mail::', self.mail)
        print('id::',self.id)

e1 = Emp('Rajiv','Patil',7020380691,'patilrajiv@gmail.com',5048)
e2 = Emp('Akshay','Jadhav','jadhavakshay@gmail.com',9263458756,3163)
e1.display()


# where we can define instance variable:= 1] inside instance method using self
#                                         2] inside constructor using self
#                                         3] outside class using object name

# 1] inside instance method using self
#-------------------------------------
class Emp:
    def __init__(self,first,last,mob,mail,id):
        test=100
        self.first = first
        self.last = last
        self.mob = mob
        self.mail = mail
        self.id = id
        self.test = test

    def display(self):
        print('first::',self.first)
        print('last::',self.last)
        print('mob::',self.mob)
        print('mail::', self.mail)
        print('id::',self.id)
        print('test::',self.test)

e1 = Emp('Rajiv','Patil',7020380691,'patilrajiv@gmail.com',5048)
e2 = Emp('Akshay','Jadhav','jadhavakshay@gmail.com',9263458756,3163)
e1.display()
print(e1.test)


# 2] inside constructor using self
# ---------------------------------------
class Emp:
    def __init__(self,first,last,mob=0,mail=0,id=0):
        self.first = first
        self.last = last
        self.mob = mob
        self.mail = mail
        self.id = id

    def display(self):
        print('first::',self.first)
        print('last::',self.last)
        print('mob::',self.mob)
        print('mail::',self.mail)
        print('id::',self.id)

e1 = Emp('Rajiv','Patil')
e1.display()

# 3] outside class using object name:-
#------------------------------------

class Emp:
    def __init__(self,first,last,mob,mail,id):
        self.first = first
        self.last = last
        self.mob = mob
        self.mail = mail
        self.id = id

    def display(self):
        print('first::',self.first)
        print('last::',self.last)
        print('mob::',self.mob)
        print('mail::', self.mail)
        print('id::',self.id)

e1 = Emp('Rajiv','Patil',7020380691,'patilrajiv@gmail.com',5048)
e1.sample = 'Python'
e1.display()
print(e1.__dict__)


# 2] static/class variable:- only one copy through out the class, define outside the method
# ========================
# class method:- used for handling class variable

class student:
    College_name = 'SGI'  #class variable
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def display(self):
        print('Name::',self.name)
        print('Surname::',self.surname)
        print('Age::',self.age)

    @classmethod
    def is_College_name(cls):
        print(cls.College_name)        # acessig class variable inside class method

a = student('Rajiv','Patil',27)
a.display()
a.is_College_name()
print(student.College_name)   # acessing class variable outside class variable


# 3] Local variable:= define within the method, scope within the method only
#------------------

def show():
    x = 10  # local variable
    print(x)

show()

def add(y):
    x = 10
    print(x+y)

add(20)




