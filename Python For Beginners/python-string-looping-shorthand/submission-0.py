def print_string_characters(word1: str, word2: str) -> None:
    for i in word1:
        print(i)
    for i in word2:
        print(i)
    pass




# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")


































""" String Looping Shorthand
Consider the following code:

my_string = "Hello"

for i in range(len(my_string)):
    print(i, my_string[i])
The output would be:

0 H
1 e
2 l
3 l
4 o
It prints the index of each character in the string along with the character itself.

But if we don't explicitly need the index, we can use a shorthand to loop through each character in the string:

my_string = "Hello"

for char in my_string:
    print(char)
This code will output:

H
e
l
l
o
Directly using the in keyword allows us to iterate through each character of the string without needing to use the index. We used the name char for readability, but you can use any name you want, like c or i.

Challenge
Implement a function called print_string_characters(word1: str, word2: str) -> None. It should print the characters of word1 separately, and then print the characters of word2 separately. Use the shorthand method to loop through each character in each word. """