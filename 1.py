'''
notes impodent points
 Data Types in Python
int: For integers (e.g., 1, -3, 100)
float: For floating-point numbers (e.g., 3.14, -0.001)
string: For strings (e.g., "Hello", "Python")
bool: For boolean values (True or False)
x= 10
print(type(x))  # Output: <class 'int'>
#a= 10
#b= 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
Print(a // b)  # Output: 3 (Floor Division)
(Floor Division) it means it will give only the integer value after division it will ignore the decimal value like 3.999 it will give only 3
print(a % b)  # Output: 1 
(Modulus) it means it will give the remainder after division like 10/3=3*3=9 remainder is 1 so it will give 1
print(a ** b)  # Output: 1000 (Exponentiation)
(Exponentiation) it means it will give the power like 10**3=10*10*10=1000 like 10 to the power 3 is 1000
x, y, z = 10, 20, 30
print(x)  # Output: 10
Print(y)  # Output: 20
print(z)  # Output: 30
x = y = z = 100
print(x, y, z)  # Output: 100 100 100
print("Age as float:", age_float)
is the name will apper in the output like "Age as float:"it will visiable in the output it is to be in the print statment inside
 swapping values it means we are exchanging the values of two variables#a = 5 b = 10 #a, b = b, a #print(a, b)  # Output: 10 5
input it means to take the input from the user like name = input("Enter your name: ") print("Your name is", name)in anouther method is it dosent take print option we have allready gave a command (input), it will take as a string only like
print(" happy birthday to my ", boy_name ) this method is also usefull it comes like  happy birthday to my  siddu this type of output in next line the total q/a is in bellow
input
oy_name = input("My booss name is : ")
print(" happy birthday to my ", boy_name )
output
My booss name is : siddu
#happy birthday to my  siddu
boy_name = input("Boy Name is : ")
girl_name = input("Girl Name: ")
boy_age = int(input("Boy Age: "))
girl_age = int(input("Girl Age: "))
age_diff = boy_age - girl_age
print(boy_name +" loves " + girl_name +
 ".Age difference is :",age_diff) in this position in old version we need to add (+) option in the moddle and it is a string i need to convert it in old version in new version 
is not needed this type ".Age difference is :",age_diff)this is new type 
in the place of tie we use in old version we use(+)symble in new version we use(,)to tie each world like this print(boy_name ," loves " , girl_name , ".Age difference is :",age_diff)
old type is below
boy_name = input("Boy Name is : ")
girl_name = input("Girl Name: ")
boy_age = int(input("Boy Age: "))
girl_age = int(input("Girl Age: "))
age_diff = abs(boy_age - girl_age)
print(boy_name +" loves " + girl_name + " Age difference is :" + str(age_diff))
in this (abs) option is add it helps that to be not giviging the (-) value like siddesh.k loves girl Age difference is :-11 in prevese method by adding the (abs)
it will give me this typr of value like siddesh.k loves girl Age difference is :11 observr that thers is no (-)in the 11 it is a (abs)
(""")
This is a multi-line comment.
It can span multiple lines.
()""")
 This is a single-line comment. It explains that the following code takes input from the user.it works as a (#)format
  (#) This is a single-line comment

  '''