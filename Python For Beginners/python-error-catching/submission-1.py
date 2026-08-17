def divide_numbers(a: str, b: str) -> None:
    
    try:
        first_number=int(a)
        second_number=int(b)
        divide=first_number/second_number
        print(divide)
    except Exception as error:
        print("An error occurred:",error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")





""" Error Catching
When an error occurs in a try block, it may be useful for us to know exactly what error occurred. This can allow us to better debug our code.

try:
    result = 10 / 0
except Exception as error:
    print("Error:", error)
The above code will catch the error and place it inside a variable called error using the as keyword. We can then print this variable to see the error message, which would be:

Error: division by zero
Challenge
Implement the function divide_numbers(a: str, b: str) -> None. It accepts two strings as arguments. You should attempt to convert the strings into integers, and then divide the first number by the second number. And then print the result.

If an error occurs, print "An error occurred:", followed by the error message. """
