# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***



def list_new():
    string = "lets do a coding challenge"
    return (string[::-1])

print(list_new())
    
# a = [11, 42, 53, 65, 99]
# a[0]    # 11
# a[-1]   # 99
# a[::2]  # [11, 53, 99]
# a[::-1] # [99, 65, 53, 42, 11]
