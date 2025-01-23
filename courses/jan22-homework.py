# Complete the function  f  so that it returns the product of a and b. Use the next cell to test the function.

def f(a,b):
    return a * b

# Complete the function g such that the input c is a list of integers and the output is the sum of all the elements in the list.

def g(c):
    return sum(c)

# Come up with a function that divides the first input by the second input:

def divide(a, b):
    return a/b

# Use the function con for the following question.
def con(a, b):
    return(a + b)

# Can the con function we defined before be used to add two integers or strings?
Yes

# Can the con function we defined before be used to concatenate lists or tuples?
Yes

# Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**

def getTotalCount(string, key):
    return string.split().count(key)


