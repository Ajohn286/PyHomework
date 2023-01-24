# QUESTIONS:
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
# ..... 

# def greeting(username):
#    return print("hello_"+username)


# name = "Austin"
# print(greeting(name))


# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
# # ..... 

# def firstodds(x):
#    return print (list(range(1,x,2)))

# print(firstodds(100))
# print(firstodds(300))

# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 
# def max_num_in_list(a_list):
#    return print(max(a_list))
# #test cases
# list = [1,2,3,4]
# list2= [6,88,44,104,1]
# print(max_num_in_list(list))
# print(max_num_in_list(list2))
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). 
# 
# def is_leap_year(a_year):
#     if(a_year % 4 == 0):
#         if(a_year % 100 != 0 or a_year % 400 == 0):
#             return True

#     else: 
#         if(a_year % 4 > 0): 
#             return False

# print(is_leap_year(1984)) #equal True
# print(is_leap_year(2001)) #equal False
# print(is_leap_year(2004)) #equal True
# print(is_leap_year(2006)) #equal False
# print(is_leap_year(2008)) #equal True
# Question 5

# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. 
# 

def is_consecutive(b):
    return sorted(b) == list(range(min(b), max(b)+1))
       


list3 =[1,2,3,8,5,6,7,4]
list4 = [1,2,3,10,5,6,7,4]
print("...")
print(is_consecutive(list3))
print(is_consecutive(list4))