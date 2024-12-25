
# Strings and Conditional Statements

# Strings =String is data type that stores a sequence of characters.

# Basic Operations

# concatenation = "hello"+"sachin" = "helloworld"
#lenght of str = len(str)

# str1 = "this is a string."
# str2 = 'ApnaCollege'
# str3 = """this is a String"""
# print(str1)
# print(str2)
# print(str3)


# CONCATENATION  = join two string.

# str1 = "hello"
# str2 = "sachin"
# finalstr = str1+str2
# print(len(str1)+len(str2))
# print(finalstr)


# INDEXING

# str = "sachinkumar"
# print(str[7])


# SLICING = Accessing parts of a string.

# str = "sachin"
# print(str[1:4])
# print(str[:4])   #[0:4]
# print(str[0:])  # [1:len(str)]



# Slicing in Negative Direction
# str = "sachin"
# print(str[-6:-1])


# String Functions

# str ="i am studying python from apna college."
# print(str.endswith("ege."))   # return true if string end with subtsring.
# print(str.capitalize())  #captilize the 1st char of the string.
# print(str.replace("python","java")) # replace with python .
# print(str.find("i"))   # find the index othe string.
# print(str.count("am"))  #count the index of the word.

# lets Practice Question

# WAP to input users first name & print its Length.

# name = input("what is your name:")
# print("Length of your name is:",len(name))


#WAP to find the occurance of '$' in a String.

# str = "hi ,$ I am the $ symbol $999."
# print(str.count("$"))


# CONDITIONAL STATEMENTS  :if-elif-else

# light = "green"
# if(light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("wait")
# else:
#     print("GO")
# print("End of Code")


# # Another Example
# age = 24
# if(age>=18):
#     print("can vote")
# elif(age<=16):
#     print("Cant not vote")
# else:
#     print("All appear")    


# WAP to Grade student based on marks.

marks = int(input("Enter the marks :"))
if(marks>=90):
    grade = "A"
elif(marks>=80 and marks <90):
    grade = "B"
elif(marks>=70 and marks <80):
    grade = "c"      
else:
    grade = "D"

print("Grade of the student ->",grade)

    