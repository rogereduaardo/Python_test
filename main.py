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

print("find index for the word cougars on:", h) #printing the index of the substring
print("Index:", h.find("cougars"))
print()

# Split the substring into list

print("before spliting the string:", h)
print("after spiiting the string:", h.split())
print()

# Regular expressions (RegEx)
# Need to import the re module

import re
print("************************** RegEx_Special_Sequences **************************")

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
print()

# Create a list

print("Creating a List of elements")
L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# List slicing

print('List slicing')
print(L[0:2])

# Extend can help tp add more elemets to a list

print('Extending the list')
L.extend(['pop',10])
print(L)

# Append adds just one element to the list

print('Appending the list')
L.append(['a','b'])
print(L)

# Change the element based on the index

print('Changing the element based on the index')
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index

print('Deleting the element based on the index')
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

print('Splitting the string')
print('hard rock')
print('hard rock'.split())

# Split the string by comma

print('Splitting the string by comma')
print('A,B,C,D')
print('A,B,C,D'.split(','))

# Copy and clone the list

A = ['hard rock'] + A
B = A
print("A:", A)
print("B:", B)
      
# Examine the copy by reference

print('B[0]:', B[0])
A[0] = 'banana'
print('B[0]:', B[0])
print("A:", A)
print("B:", B)

# Clone (clone by value) the list A

B = A[:]
print("A:", A)
print("B:", B)
print('B[0]:', B[0])
A[0] = 'hard rock'
print('B[0]:', B[0])
print()

# Creating tuples

tuple1 = ("disco",10,1.2)
print(tuple1)
print(type(tuple1))

# Index for tuples is the same, negative index can also be used

print(tuple1[0]) #print(tuple1[-1])
print(tuple1[1])
print(tuple1[2])

# Print the type of value of each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))      

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Slicing tuples

print(tuple2[0:3])

# Get the length of tuple

print(len(tuple2))

# Sorting tuples

Ratings = (0,9,6,5,10,8,9,6,2)
print(Ratings)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# Create a nest tuple

NestedTuple = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
print(NestedTuple)

# Printing elements on each index 

print("Element 0 of Tuple: ", NestedTuple[0])
print("Element 0 of Tuple: ", NestedTuple[1])
print("Element 0 of Tuple: ", NestedTuple[2])
print("Element 0 of Tuple: ", NestedTuple[3])
print("Element 0 of Tuple: ", NestedTuple[4])

# Printing elements on a nested index

print("Element 2,0 of Tuple: ", NestedTuple[2][0])
print("Element 4,1,1 of Tuple: ", NestedTuple[4][1][1])

# Print the element of string on a nested tuple

print("Element 2,0,1 of Tuple: ", NestedTuple[2][0][1])

# Find the index of 's' in "disco":

print("disco".find('s'))

# Create the dictionary
Dict = {
"key1": 1, "key2": "2", "key3": [3, 3, 3], 
"key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

# Access to the value by the key
print(Dict["key1"])
print(Dict[(0, 1)])

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
"The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
"Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
"Saturday Night Fever": "1977", "Rumours": "1977"}

# Get value by keys
print(release_year_dict['Thriller']) 
print(release_year_dict['The Bodyguard'])
print("\n")

# Get all the keys in dictionary
print(release_year_dict.keys()) 
print("\n")

# Get all the values in dictionary
print(release_year_dict.values())
print("\n")

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'

print(release_year_dict)
print("\n")

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])

print(release_year_dict)
print("\n")

# Verify the key is in the dictionary
print('The Bodyguard' in release_year_dict)
print("\n")

# Example

# Create an emtpy dictionary
inventory = {}

# Store the first product details in variable
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

# Add the details in inventory
inventory["ProductNo1"] = ProductNo1
inventory["ProductNo1_quantity"] = ProductNo1_quantity
inventory["ProductNo1_price"] = ProductNo1_price
inventory["ProductNo1_releaseYear"] =ProductNo1_releaseYear

# Store the second product details in variable
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

# Add the details in inventory
inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_releaseYear"]= ProductNo2_releaseYear

# Display the products in the inventory
print(inventory)
print("\n")

# Chek if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory
print("ProductNo1_releaseYear" in inventory)
print("ProductNo2_releaseYear" in inventory)

# Delete release year of both products from the invenotry
del(inventory['ProductNo1_releaseYear'])
del(inventory['ProductNo2_releaseYear'])   