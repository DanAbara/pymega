# use the open() function to open a file
myfile = open("files/notes.txt") # open the file by creating a file object in RAM
# print(myfile.read())
# print(myfile.read())

# to print the contents out multiple times considering that the cursor will
# be at the end of the doc after print() statment on line 3
content = myfile.read()
print(content)
print(content)

# to close the file and remove the object from RAM
myfile.close()


# Alternative and better way is by using 'with' context manager
with open("files/notes.txt") as myfile:
    content = myfile.read()

print(content)

# writing content to a file using the mode argument (see help(open)) of the open() func
with open("files/veggies.txt", "w") as myfile:
    myfile.write("Tomatoes\nCucumber\nOnion\n") # \n means newline
    myfile.write("Garlic")


# appending text to an existing file. We use mode options see 'character meaning section' under help(open)
# using the mode option 'a' would open for only appending and you can't read the file
with open("files/veggies.txt", "a+") as myfile: # open in append mode for reading and writing
    myfile.write("\nNewline Okra")
    myfile.seek(0) # send cursor back to beginning
    content = myfile.read() # read contents of myfile    

print(content)
