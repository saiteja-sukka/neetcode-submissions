variable=5
print(type(variable))
variable = 7.88
print(type(variable))
variable = True
print(type(variable))
variable = "name"
print(type(variable))
variable = [7.9,5]
print(type(variable))










""" Dynamic Typing
In Python a single variable's type can change throughout the code. This is called dynamic typing. For example, the following code will run without any errors:

variable = 10         # int type
variable = "Hello"    # str type
variable = [1, 2, 3]  # list type
Not all languages support dynamic typing. In some languages, a variable's type must be explicitly declared and cannot be changed. This is called static typing. For example, in Java, the following code will cause an error:

int variable = 10;
variable = "Hello";  // Error: incompatible types
Challenge
Update the code on the right, without removing any lines, so that the output is:

<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
<class 'list'>

Is dynamic typing a good idea?
Dynamic typing should generally be avoided when possible. This means you should avoid changing a variable's type throughout your code. If you do, you may not know what type a variable is at any given time, which can lead to bugs and make your code harder to understand.

Static typing is employed by many languages on purpose. It can help catch errors early, make code easier to read, and improve performance.

Each typing system has it's own advantages and disadvantages. Dynamic typing is flexible, but can be error-prone. Static typing is safer, but can be inflexible. """