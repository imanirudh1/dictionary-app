import json
from difflib import get_close_matches
word=input('enter the word : ').lower()
data=json.load(open('data.json'))

#print(result)
def translate(word):
    if word in data:
        result=data[word]
        return result
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.title() in data:
        return data[word.title()]    
    elif word.upper() in data:
        return data[word.upper()]            
    elif len(get_close_matches(word,data.keys()))>1:
        a=input(f'Do you mean {get_close_matches(word,data.keys())[0]} ?')
        while (a != 'y') and (a!='n'):
            print('we didn\'t understand your entry pls enter again')
            a=input()
        if a =='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif a=='n':
            return 'Sorry the word doesnot exist'    

    else:
        return 'word does not exist'

output=translate(word)
if type(output)== list:
    for i in output:
        print(i)
else:
    print(output)