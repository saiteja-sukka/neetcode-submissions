def print_string_characters(my_string: str) -> None:
    for i in range(len(my_string)):
        print(my_string[i])
    pass


# do not modify below this line
print_string_characters("Hello, World!")
print_string_characters("Good Job!")

















""" String Looping
What if we want to access each character in a string separately? With our knowledge of loops, indexing and the len() function we can now accomplish this.

my_string = "Hello, World!"

length = len(my_string) # 13

for i in range(length):
    print(my_string[i])
Remember that the range(13) function will generate a sequence of numbers from 0 to 12, not including 13.
This is perfect, the first character of our string is at index 0, and the last character of our string is at index 12.
We can now use the index i to access and print each character of the string.
Challenge
Implement a function called print_string_characters(my_string: str) -> None. It takes a string as a parameter and prints each character of the string separately. """