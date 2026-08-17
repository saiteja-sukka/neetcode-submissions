def add_two_numbers() -> int:
    user_input=input()
    sum=0
    for i in user_input.split(","):
        sum+=int(i)
    return sum
    pass



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

























""" Reading Input Practice
Implement the function add_two_numbers() -> int. It doesn't have any parameters because you will be reading from stdin. The function should read one line from stdin, which contains two integers separated by a comma. The function should return the sum of the two integers.

The stdin to your program will be:

1,2
3,4
10,25
1032,1272 """