# define a function that takes in temperatures and checks whether it is warm or cold
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# input function is used to get data from the user
user_in = float(input("Enter temperature:")) # float() or int() converts the inputed string to a floating point number
print(weather_condition(user_in))

# print a user's name using string formatting.
user_in1 = input("Enter your name: ")
message1 = "Hello %s!" % user_in1 # str formatting
message2 = "Hello {}!".format(user_in1) # str formatting - I like this
print(message1)
print(message2)

# string formatting with multiple variables
name = input("Enter your firstname: ")
surname = input("Enter your surname: ")
message1 = "Hello %s %s!" % (name, surname)
message2 = "Hello {} {}!".format(name, surname)
print(message2)
print(message2)

# for loops: runs until a container (a list, dictionary etc) is exhausted/empty.
# looping through a list
monday_temp = [2,3.4,6.7,8.5,9.2]
for temps in monday_temp:
    print(round(temps))
    print('Done')

for letter in 'Hello':
    print(letter.upper())

# looping through a dict
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
for grades in student_grades.items(): # could be items(),keys() or values()
    print(grades)

# for loop on dict with string formatting
for key, value in student_grades.items():
    print("{} has a grade of {}".format(key, value))

# while loops: runs as long as a condition is true and only stop when the condtion is false.
username = " "
while username != "pypy":
    username = input("Enter your username: ")

# the above snippet may be achieved alternatively by:
while True:
    username = input("Enter your username: ")
    if username == "pypy":
        break
    else:
        continue







