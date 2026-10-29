#!/usr/bin/env python3
import sys
def average(scores_dict):
    # """
    # Takes a dictionary of student names and their scores,
    # and returns the average score of the class.
    # """
    # Sum up all the scores (the dictionary values)
    total_score = sum(scores_dict.values())
    
    # Get the total number of students (the dictionary keys)
    total_students = len(scores_dict)
    
    # Calculate and return the average
    return (total_score / total_students)

# --- Example Usage (Matching the assignment prompt) ---
if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")