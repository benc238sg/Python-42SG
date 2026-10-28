#!/usr/bin/env python3
import sys
import re

# Check if the number of passed arguments is exactly 2
# len(sys.argv) must equal 3 (script name + keyword + target string)
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    
    # Find all non-overlapping occurrences of the keyword
    # re.escape ensures special regex characters in the keyword are treated as literal text
    #matches = re.findall(re.escape(keyword), search_string)
    matches = re.findall(keyword, search_string)
    # If there are no matches, or if the keyword wasn't found, print "none"
    if not matches:
        print("none")
    else:
        print(len(matches))
    #    print(matches)