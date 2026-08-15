def first_n_characters(s: str, n: int) -> str:
    return(s[:n])
    pass

def last_n_characters(s: str, n: int) -> str:
    return(s[len(s)-n:len(s)])
    pass


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))





































""" String Slicing Part 2
With string slicing we are actually not required to specify either the start or the end index.

If we don't specify the start, it's equivalent to starting from the beginning of the string.

my_string = "NeetCode"

print(my_string[:3])  # Output: Nee

print(my_string[0:3]) # Output: Nee
If we don't specify the end, it's equivalent to ending at the end of the string.

my_string = "NeetCode"

print(my_string[4:])  # Output: Code

print(my_string[4:8]) # Output: Code
If we don't specify either, we get the entire string.

my_string = "NeetCode"

print(my_string[:])  # Output: NeetCode
print(my_string)     # Output: NeetCode
Challenge
Implement the two functions on the right as follows:

first_n_characters(s: str, n: int) -> str should return a string with the first n characters from s. You may assume that the length of s is greater than or equal to n.
last_n_characters(s: str, n: int) -> str should return a string with the last n characters from s. You may assume that the length of s is greater than or equal to n.
Hint: If we want the last 1 character from a string s, we would start at index = len(s) - 1. If we want the last 2 characters, we would start at index = len(s) - 2. """