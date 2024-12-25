# Lists in PYTHON 

# marks = [94.4,90,66.6,45.3,89.4]
# print(marks)        #   94.4,90,66.6,45.3,89.4
# print(type(marks))  #   <class 'list'>
# print(marks[0])     #   94.4
# print(len(marks))   #    5

# Lists  Slicing

# marks = [94.4,90,66.6,45.3,89.4]
# print(marks[1:4])  #[90, 66.6, 45.3]
# print(marks[:4])  #[94.4, 90, 66.6, 45.3]
# print(marks[1:len(marks)])  #[90, 66.6, 45.3, 89.4]
# print(marks[-3:-1])      #[66.6, 45.3]


#  List Method

# list = [2,1,3]
# list.append(4)   #add one element at the end.
# print(list)

# list.sort()  # sort in asecnding order
# print(list)

# list.sort(reverse=True)  #sort in descending order
# print(list)

# list.reverse()   #reverse the list
# print(list)

# list.insert(1,5)   #  (index,element) add
# print(list)

# list.remove(1)   # remove first occurence of element
# print(list)

# list.pop(2) #  remove element from index
# print(list)



# Tuples in Python

# tup = [23,34,12,24,4,5]
# print(tup[0])  #23
# print(tup[1])  #34
# tup = ()
# print(tup)     #()
# print(type(tup))   #<class 'tuple'>



# Tuples Methods
tup = (2,1,3,1)
print(tup.index(1))  # return index of first occurence.
print(tup.count(1))  # Count total occurence

