# This is a Test
# main.py

# Hello world test
print("Hello World!")
print()

#Information on strings and examples

#Concatening strings vs Integers
a = "1"
b = "2"
c = a + b #returns a concatenated string not the sum of the two integers

d = 1
e = 2
f = d + e #returns the sum of the two integers

#Print to test

print(c) #prints the concatenated string
print(f) #prints the sum of the two integers
print()

#Using slicing to print the certain value of a string

g = "ABCDEFGHIJKLMNOPQRS"

#slicing the first 3 values
g[0:3]

#printing to check
print(g)
print("the length of g is", len(g))
print(g[0:3])
print(g[15:18])

#Using stiding to print a pattern of values ex. every other value

print(g[::2]) #printing only every other value
print(g[::5]) #printing only every fith value
print(g[3:16:3]) # printing avery third value from the third value to the 16th value
print()
#Escape sequences
#using r before a string will remove the escape sequences

print("This is a test \nThis is only a test") #string with escape sequences
print(r"This is a test \n This is only a test") #string with r displaying raw values  
print()
# String Manipulaion Operations

# Converting all character to uppercase 

h = "go cougars" # asiigning a string to a variable
print("before upper", h) #printing the string to test
print("after upper", h.upper()) #printing the string after the operation
print()

# Replace an old string with a new string

print("before replace:", h) # printing the string to test
print("after replace:", h.replace("cougars","comets"))
print()

# Find the substring in the string

print("find index for the word cougars:", h.find("cougars")) #printing the index of the substring
print()

# Split the substring into list

print("before spliting the string:", h)
print("after spiiting the string:", h.split())
print()

# Regular expressions (RegEx)
# Need to import the re module

import re

# Define the pattern to search for
print("search for the word cougars on:", h)


# Use the search() function to search for the pattern in the string
result = re.search("cougars", h)

# Check if the pattern was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# RegEx with special sequences


#Special 
#Sequence	           Meaning	                            Example
#\d	      Matches any digit character (0-9)	                "123" matches "\d\d\d"
#\D	      Matches any non-digit character	                  "hello" matches "\D\D\D\D\D"
#\w      	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
#\W	      Matches any non-word character                  	"@#$%" matches "\W\W\W\W"
#\s	      Matches any whitespace character (space, tab)	    "hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
#\S	      Matches any non-whitespace character	            "hello_world" matches "\S\S\S\S\S\S\S\S\S"
#\b	      Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
#\B	      Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
print(text)
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# RegEx expression split

print(h)
print(re.split(r"\s", h))

# RegEx replace

print(h)
print(re.sub("cougars", "comets", h))