# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***

# initial try
# def list_new(number):
#     list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
#     return list_new = list[number::]
# print(list_new(number))

# solution with notes

# define function
def list_new(number):
    #set list with our fibonacci values
    list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    #asking function to return an array, 1. start point at 0, 2. stop at defined index number,
    #3. no defined step
    return (list[:number])
# this is how we call the function, and insert the number
print(list_new(4))
# this returns an example result of:
# [0, 1, 1, 2]
