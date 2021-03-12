import re

text = "The rain in Spain"


#Search Function 
x = re.search("^The.*Spain$", text) # In a regular Search , it will return the a Match object if there is a match
if x:
    print("Yes, We have match!")

else: print("No Match")

#Find All Function
x = re.findall("ai", text)
print(x)

# #Split Function
x = re.split("\s", text, 1) # the 1 controls the number of occurences by maxsplit parameter
print(x)

# #Sub Function
x = re.sub("\s", "9", text, 2)  # the two replaces the first 2 occurences that there is 
print(x)

#MATCH OBJECT

#Span Method
x = re.search(r"\bS\w+", txt) #The regular expression looks for any words that starts with an upper case "S":
print(x.span())

#String Method
x = re.search(r"\bS\w+", txt) #Print the string passed into the function:
print(x.string)

#Group Method
x = re.search(r"\bS\w+", txt) #The regular expression looks for any words that starts with an upper case "S":
print(x.group())