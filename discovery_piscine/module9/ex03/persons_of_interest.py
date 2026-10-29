#!/usr/bin/env python3
import sys

def famous_births(figures_dict):
    """
    Sorts a nested dictionary of historical figures by their birth dates
    and prints them out in a formatted string.
    """
    # Grab the inner dictionary details (the values) and sort them by the birth year string converted to an integer
    sorted_figures = sorted(figures_dict.values(), key=lambda info: int(info["date_of_birth"]))
    
    # Loop through the sorted list and print each formatted string
    for info in sorted_figures:
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

# --- Example Usage (Matching the assignment prompt) ---
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    
    famous_births(women_scientists)