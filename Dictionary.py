import json
from difflib import get_close_matches
# Loading the data 
data = json.load(open("data.json"))

def translate(w):
    # Making the program case Insensitive
    w = w.lower()
    if w in data:
        return data[w]
    # Checking for the close matches for the words.
    elif len(get_close_matches(w, data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y for Yes and N for No : " %get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Please check the word."
        else:
            return "We didn't understnd your entry."

    else:
        return "The word doesn't exist. please check the word."

word = input("Enter word: ")
# Making output more User friendly
output=(translate(word ))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)