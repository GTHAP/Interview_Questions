# This is one of my ealy attempts at solving a coding challege
# I appended the string to a list which made it easy to manipulate the charachters and then joined them back together into a string
# This is not a good piece of code and I will improve upon it

def breakCamelCase(string):
    tempstring = []
    breakcamelcase = ""
    for i in string:
        tempstring.append(i)
    for i in range(1, len(tempstring) + 1):
        if tempstring[i - 1] != " ":
            if tempstring[i] == str.upper(tempstring[i]): 
                tempstring.insert(i, " ") 
        if tempstring[i] == " ":
            i += 2
            continue
    for i in tempstring:
        breakcamelcase = "".join(map(str, tempstring))
    return breakcamelcase

string = "newCodeInPythonLanguage"
breakCamelCase(string)
