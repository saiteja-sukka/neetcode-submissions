def concatenate(s1: str, s2: str) -> str:
    if len(s1)+len(s2)<=10:
        return(s1+s2)
    return("Too long!")
    pass




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))







































""" String Concatenation
In Python, concatenation is the process of combining two or more strings into a single string. Python provides the + operator for concatenating strings. When you use the + operator with two strings, Python joins them together to create a new string.

str1 = "Hello, "
str2 = "world!"
print(str1 + str2) # Output: Hello, world!
In this example, str1 and str2 are concatenated together using the + operator, resulting in the string "Hello, world!".

Challenge
Implement the function concatenate(s1: str, s2: str) -> str. It accepts two strings as parameters and returns a new string that is the concatenation of the two input strings. If the length of the string after concatenating them is greater than 10, return "Too long!".

For example,

If you call concatenate("Good ", "job!"), it should return "Good job!".
If you call concatenate("Goodbye, ", "world!"), it should return "Too long!". """