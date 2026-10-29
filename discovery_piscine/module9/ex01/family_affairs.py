#!/usr/bin/env python3
import sys
def find_the_redheads(family_dict):
    # """
    # Filters a family dictionary to find members with red hair 
    # and returns a list of their first names.
    # """
    # filter() loops through the dictionary keys (the first names).
    # The lambda function checks if that person's hair color is "red".
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    # lambda is a function that simplify like below.
    # def check_hair(name):
    # return family_dict[name] == "red"
    
    # Convert the filter object back into a standard list before returning
    return list(redheads)

# --- Example Usage (Matching the assignment prompt) ---
if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red",
        # "victor": "black",
        # "justin": "red"
    }
    
    print(find_the_redheads(dupont_family))