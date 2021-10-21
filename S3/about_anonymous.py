"""
Creating a function normally (using def) assigns it to a variable with its name automatically.
Python allows us to create functions on-the-fly, provided that they are created using lambda syntax.

This approach is most commonly used when passing a simple function as an argument to another function.
The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon,
and the expression to evaluate and return.

Functions created using the lambda syntax are known as anonymous.
"""

my_anonymous_f = lambda x: x * 2, 5

print(my_anonymous_f)

"""
Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression 
-- usually equivalent to a single line of code.
"""