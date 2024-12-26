# # Dictionary in PYthon

# student={
#     "name:": "sachin",
#     "Cgpa" : 8.1,
#     "Marks": [98,97,87],
# }
# print(student)  #{'name:': 'sachin', 'Cgpa': 8.1, 'Marks': [98, 97, 87]}
# print(type(student))  #<class 'dict'>


# # Nested Dictionary in Python
# student={
#     "name:": "sachin",
#     "Cgpa" : {
#         "chem": 98,
#         "phy":97,
#     }
# }
# print(student) #{'name:': 'sachin', 'Cgpa': {'chem': 98, 'phy': 97}}


# Dictionary Methods

# student={
#     "name:": "sachin",
#     "Cgpa" : {
#         "chem": 98,
#         "phy":97,
#     }
# }
# print(student.keys())   #dict_keys(['name:', 'Cgpa'])
# print(student.values())  #it return all values
# print(student.items())   #return all (key,value) pair as tuples.
# print(student.get("key")) #return the key a/c to value
# print(student.update())   #insert the specified items to the dictionary


# Set in Python

nums = {1,2,3,4,2,3,4}
print(nums)         #{1, 2, 3, 4}
print(type(nums))   #<class 'set'>
nums.add(5)
print(nums)        #  add new element is 5 {1, 2, 3, 4, 5}


nums.remove(5)
print(nums)        # remove the element from the index {1, 2, 3, 4}

nums.clear()
print(nums)        #set()



nums = {1, 2, 3, 4, 5}
nums.pop()
print(nums)  #   remove from index 1 ,  {2, 3, 4, 5}


