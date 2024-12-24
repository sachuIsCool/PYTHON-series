# Print a message (commented out)
# print("hello sachin")

# Variable declarations
name = "sachin"
age = 21
old = False
a2 = None
price = 23.23

# Check the datatype for each variable
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
print(type(old))    # <class 'bool'>
print(type(a2))     # <class 'NoneType'>

# Datatypes
# Strings can be represented using "", '', or ''' '''
name1 = "sachin"
name2 = 'sachin'
name3 = '''sachin'''
print(name1)  # sachin
print(name2)  # sachin
print(name3)  # sachin

# Print the sum of two numbers in Python
a = 2
b = 3
sum = a + b
print(sum)  # 5

# Comments in Python
# Single-line comments start with #
# Multiline comments are enclosed in """ """

# Operators
# Arithmetic Operators
a1 = 3
b1 = 2
print(a1 + b1)  # Addition: 5
print(a1 - b1)  # Subtraction: 1
print(a1 * b1)  # Multiplication: 6
print(a1 / b1)  # Division: 1.5
print(a1 % b1)  # Modulus: 1
print(a1**b1)   #power:9



# Relatioal operator :compared betweem two operator(==,!=,<,>,>=,<=)
a2 = 50
b2 = 20
print(a2==b2)  #False
print(a2!=b2) #true
print(a2<b2)  #false
print(a2>b2)  #true


# Assignment Operator
num = 10
num = num + 10    #10+10=20
print(num)


# Logical Operator(it work on boolen Value)
print(not False)
print(not True)
val1 = 50
val2 = 30
print(not False)
print(not (a > b))
val1 = True
val2 = True
print("AND opertor:", val1 and val2)

print("OR opertor:", val1 or val2)


# Type conversion 
a4 = 2   #this integer value 
b4 = 4.80  #this float value
sum = a4 + b4 
print(sum)  # total =6.80


# a5 = "2"  # this string value / 
# b5 = 4.45
# sum1 = a5 + b5
# print(sum1)  #output is given that error  it is not possible 
#   can only concatenate str (not "float") to str


#Type casting
a6 = float("2")
b6 = 4.45
print(type(a6))  #<class 'float'>
sum = a6+b6 
print(sum)  #  total = 6.45

#  it is not possiblte converted the string into the float
# a6 = float("sachin")
# b6 = 4.45
# print(type(a6))  #<class 'float'>
# sum = a6+b6 
# print(sum)  #  total = 6.45



# Input in python  taking from the user


# name = input("enter the name:")
# print("wecome",name)

# #  result for input() is always a string

# val = input("enter the some value")
# print(type(val),val)  #"25", "99.99"

# int(input())    /int
# int("4")
# val = int(input("enter some value"))
# print(type(val),val)




# print a program to input 2 number & print thier sum

# first = int(input("enter the first number"))
# second = int(input("enter the second number"))
# print("sum=", first+second)


# WAP to input side of a square & Print its Area.

# side = int(input("Enter the Side "))
# print("Area=",side*side) 


#WAP to input 2 FLoating Point number & Print their Average.
# first = float(input("Enter the firat number  "))
# second = float(input("Enter the Second Number "))
# print("Average=",(first+second)/2)


# WAP  a program to 2 input 2 numbers,a and b. print True if a is greater than equal to b.if not Print False.
first = int(input("enter the  First Number"))
second = int(input("Enter the second Number"))
print(first>=second)
