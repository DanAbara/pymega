# dir(__builtins__) tells you all the inbuilt functions, methods and types
# dir(list) or dir('type') tells you the methods in the type list.
# help('type.method') tells you what the specific method does and a simple syntax

student_grades1 = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9] # define list
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5} # define dict
print(student_grades)

mysum = sum(student_grades.values()) # sum values in list named student_grades
length = len(student_grades) # length of list named student_grades
meean = mysum/length # mean
print(meean)
print(student_grades.keys()) # keys(),values() are methods uner the dict type and can be checked using dir(dict) and help(dict.keys)

max_val = max(student_grades1) # use built in func 'max' to obtain maximum value in a list
print(max_val)

student_count10 = student_grades1.count(10.0) # use count() method of lists to obtain the count of 10.0 in the list 
print(student_count10)

uname = "PyThon3"
print(uname.lower()) # use the lower() method of string to obtain the lowercase of the string 'uname'

rainfall = [10.1, 9, 'no data', [1, 2, 3]]
rainfall.append(3.5) # use the append() method of list type to add an element 3.5 to the list
print(rainfall) 

# accessing list items
print(rainfall.__getitem__(1)) #get the value in index 1
print(rainfall[1]) #shortcut for the code 

# slices in lists
print(student_grades1[1:4]) # extract items on index 1 to index 3. The upper limit is never included
print(student_grades1[0:3]) # extract index 0 to index 2.
print(student_grades1[:3]) # same as immediate line above but specifies extracting from beginning
print(student_grades1[6:10]) # extract from index 6 to 9
print(student_grades1[6:]) # extract from index 6 to the end, which is same result as immediate line above

# negative indexing
print(student_grades1[-1]) # extract last item. The last item in a list has an index -1
print(student_grades1[-5:]) # print last 5 items

# accessing characters in strings
mystr = 'hello'
print(mystr[1]) # returns e - works just like lists
print(mystr[0:3]) # returns hel
print(rainfall[2][3:5]) # returns index 3 of the list which is a string 'no data' and then extracts index 3 and 4 of 'no data' which returns da)

# accessing dict items
print(student_grades["Mary"]) # dicts have keys instead of indexes. 