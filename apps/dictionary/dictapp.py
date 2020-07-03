import json # import json library to read source data
import difflib
from difflib import get_close_matches # for getting the best match from a comparison

# 1 load json data using json
data = json.load(open("dictdata.json"))

# 2 function to return definition of a word
def showdef(word):
    word = word.lower() # 4 check for case sensitivity eg. boLD, BOLD, bOLd, by converting all words to lowercase any such words
    
    if word in data.keys(): # 3 add if condition to check for nonexisting words
        return data[word] # no need to put quotes "rain" since the word is definitely a string as it is comping from input()
    elif word.title() in data.keys(): # 9 fix proper noun bug, by checking for init caps
        return data[word.title()]
    elif word.upper() in data.keys(): # 10 fix acronyms like USA/NATO Bugs by checking that they are all uppercase
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0: # 5. check the best match
        response = input("Do you mean the word '{}' instead? yes or no: ".format(get_close_matches(word,data.keys())[0])) # 6 ask a user for input
        if response.lower() == "yes" or response.lower() == "y": # 7 if constructs to respond to user input
            return data[get_close_matches(word,data.keys())[0]]
        elif response.lower() == "no" or response.lower() == "n":
            return "\nThe word you have entered does not exist. Please double check and re-enter a valid word."
        else:
            return "I didn't understand your entry."
    else:
        return "\nThe word you have entered does not exist. Please double check and re-enter a valid word."

search = input("Enter a search term: ")
output = showdef(search)

# 8 make the output neater and account for when the dictionary value has only one item (is a string) 
# versus when it has multiple items (when it is a list)
if isinstance(output,list):
    for eachoutput in output:
        print("\n{}".format(eachoutput))
else:
    print("\n{}".format(output))

# check pythonhow.com for some good challenges and code


