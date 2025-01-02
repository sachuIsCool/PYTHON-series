#  Loops in Pyhton

# count =1
# while count <= 5 :
#     print("sachin")
#     count = count+1

# print(count)

# print numbers from 1 to 5 
# i=1
# while(i<=5):
#     print(i)
#     i=i+1
   

#  practice Question

# print numbers from 1 to 100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1

# print numbers from 100 to 1
# i=100
# while(i>=1):
#     print(i)
#     i=i-1

# print the multiplication table of a number n.

# i=1
# while i<=10:
#     print(4*i)
#     i=i+1

# using for Loop
# for i in range(1,11):
#     print(3*i)
# print("over")

# print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx = idx+1


# search for a number X in the tuple using loop:
# [1,4,9,16,25,36,49,81,100]

# nums = (1,4,9,16,25,36,49,81,100 ,36)
# x=36
# i=0 
# while i< len(nums):
#     if(nums[i] == x):
#         print("Found at Index",i)
#     else:
#         print("finding..")
#     i = i+1        


# break =  it is used to terminate the loop when encountered.
# contiune = it is used terminate in the current ilteration and continues  execution of the loop with the next ilteration.
# i = 0
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
    
#     i=i+1     

i = 0
while i <= 5:
  
    if(i == 3):
        i = i + 1
        continue
    print(i)
    i=i+1        

