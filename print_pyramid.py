# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***

# n is the number we'll pass in
def pyramid(n):
    # for each instance of n until i+1 = n
    # but how does it know to stop?
  for i in range(n):
      print('#' * (i+1))

print(pyramid(4))
