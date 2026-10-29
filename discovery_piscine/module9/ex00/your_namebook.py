#!/usr/bin/env python3
import sys
def array_of_names(name_dict): 
    full_names = []
    for first_name, last_name in name_dict.items(): #this is how you handle dictionary
        # Capitalize the first letter of both first and last names
        formatted_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(formatted_name) #This line add the formatted name into the set. 
    return full_names

# --- Example Usage (Matching the assignment prompt) ---
# if __name__ == "__main__":
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier", 
    # "benny": "chua",
    # "thomas": "edison"
    }
    
print(array_of_names(persons)) #print the array {persons} after going thru the function()
# In Python, a function is a standalone block of code, \
# a class is a blueprint for creating objects, 
# an object is a specific instance of a class, 
# a dictionary is a data structure storing key-value pairs, and 
# a method is a function that belongs inside a class and operates on an object.
# """
    # Takes a dictionary of first and last names, capitalizes them,
    # and returns a list of full names.
    # """