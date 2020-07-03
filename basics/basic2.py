# functions
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 3, 5, 7])) # compute the mean of the inputed list
print(type(mean), type(sum)) # check the types of mean and sum

# using conditionals
def mean2(testclass):
    if isinstance(testclass, dict):
        mymean = sum(testclass.values()) / len(testclass)
    else:
        mymean = sum(testclass) / len(testclass)

    return mymean

monday_temp = [8.8, 9.9, 9.1] # define list
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5} # define dict

print(mean2(student_grades)) # compute mean of a dictionary
print(mean2(monday_temp)) # compute mean of list