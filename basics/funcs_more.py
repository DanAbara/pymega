# functions with more than one argument
def area(a, b):
    return a * b # compute an area of sizes a x b

print(area(4,5)) 

# keyword and non-keyword arguments, default and non-default params
print(area(b=5,a=4)) # this uses keyword arguments or non-positional arguments, position doesn't matter.

# this next snippet uses non-keyword arguments or positional arguments. 
# Python assigns the inputs to the function based on their positions so position matters.
# the first item 5 is assigned to a, and the second item 4 is assigned to b as per the function definition
print(area(5,4)) 


# functions with default (initialized) values. non-default values must be defined in a function before default values
def circ(r,p=3.142,task="ar"):
    # compute circumference of circle
    if task == "cir":
        return "The circumference of the circle is {}".format(2 * p * r) # compute circumference of circle
    elif task == "ar":
        return "The area of the circle is {}".format(p * r * r) # compute area of circle

# compute circmumference using a mix of positional (non-keyword args), keyword argument and modifying the default value
print(circ(1,task="cir")) # compute the circumference

# compute area using a mix of positional (non-keyword args) and default values of pi and the task specification
print(circ(2)) # compute the area


# functions with arbitrary number of non-keyword arguments just like the print() function
def mean(*args): 
    return sum(args) / len(args)

print(mean(1,2,3,5))


# functions with arbitrary number of keyword arguments
def meanb(**kwargs):
    return kwargs

print(meanb(a=1,b=2,c=3)) # must be called using keywords