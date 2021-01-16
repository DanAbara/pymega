# create a sentence maker function
def sentence_maker(phrase):
    interro = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interro) or phrase.capitalize():
        return "{}?".format(capitalized) # for the case where the input starts with a who, what or why
    else:
        return "{}.".format(capitalized) # for every other case

outphrase = []
# ask for input until "\end" is entered by the user
while True:
    inphrase = input("Say something: ")
    if inphrase == "\end":
        break
    else:
        outphrase.append(sentence_maker(inphrase)) # append each user input to outphrase list

print(" ".join(outphrase)) # user friendly output print of outphrase list
