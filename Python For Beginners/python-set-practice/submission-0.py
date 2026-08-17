from typing import List

def contains_duplicate(words: List[str]) -> bool:
    sets=set(words)
    if len(sets)== len(words):
        return False
    return True
    pass

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))




































""" Implement the function contains_duplicate(words: List[str]) -> bool. It takes a list of strings words and returns True if there are any duplicate strings in the list, and False otherwise.

Note: There are many ways to solve this problem, so feel free to be creative. """