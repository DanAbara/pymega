temps = [221, 234, 340, 230] # stored as whole nos and not floating point temps to save space

# method 1 - deducing the actual temperatures
new_temps = [] # initialise a new list

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# method 2 - an alternative and neater way to do it using 'list comprehension'
new_temps2 = [temp / 10 for temp in temps] # like a reversed for loop or inline for loop
print(new_temps2)

# if conditionals in list comprehensions
tempsb = [221, 234, 340, -9999, 230]
new_tempsb = [temp / 10 for temp in tempsb if temp != -9999] # convert all list values except the -9999 value
print(new_tempsb)

# if conditionals with if-else for multi conditions
# to replace -9999 in the list above
new_tempsc = [temp / 10 if temp != -9999 else 0 for temp in tempsb] # ie where temp = -9999 return 0
print(new_tempsc)

# or - this does sane as kube 22 above
new_tempsc2 = []
for temp in tempsb:
    if temp != -9999:
        new_tempsc2.append(temp / 10)
    else:
        new_tempsc2.append(0)

print(new_tempsc2)
