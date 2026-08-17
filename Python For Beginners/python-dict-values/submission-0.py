from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values=list(age_dict.values())
    return values    
    pass

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))









































""" Dict Values
Another way of iterating over a dictionary is by using the values() function. This function allows us to loop over the values in the dictionary without needing to access the keys.

my_dict = {"a": 1, "b": 2, "c": 3}

for value in my_dict.values():
    print(value)
A useful use case for this is when we want to convert the values of a dictionary into a list. This can be done by using the list() function.

my_dict = {"a": 1, "b": 2, "c": 3}

values = list(my_dict.values())

print(values) # Output: [1, 2, 3]
Challenge
With this in mind, once again implement the get_dict_values(age_dict: Dict[str, int]) -> List[int] function. It accepts a dictionary of names and ages and should return a list of the ages. """