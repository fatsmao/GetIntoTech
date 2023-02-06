# Creating two variables

first_name = "Fatma";
last_name = "Sadiq";

# Print command outputs code into the terminal

print(first_name + " " + last_name);

#Python has 4 built in data types used to store collections of date.
#List
#Tuple
#Dictionary
#Set

# Lists are created using square brackets.

name = [first_name, last_name];

print(name);

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

full_name = {
    "first" : "Fatma",
    "last" : "Sadiq"
}

print(full_name);

# Tuple - used to store multiple items in a single variable. A collection which is ordered and unchangeable.

my_name = ("Fatma", "Sadiq");
print(my_name);

# Set - used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable, and unindexed.
# *Set items are unchangeable, but you can remove items and add new items.

full_name = {"Fatma", "Sadiq"}
print(full_name);

