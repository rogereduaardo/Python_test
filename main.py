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

# String Manipulaion Operations

# Converting all character to uppercase 

h = "go cougars" # asiigning a string to a variable
print("before upper", h) #printing the string to test
print("after upper", h.upper()) #printing the string after the operation
print()

# Replace an old string with a new string

print("before replace:", h) # printing the string to test
print("after replace:", h.replace("cougars","comets"))

# Find the substring in the string

print("find index for the word cougars:", h.find("cougars")) #printing the index of the substring

#Split the substring into list
