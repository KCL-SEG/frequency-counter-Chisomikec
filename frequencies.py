"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        key = str(item) if not isinstance(item, str) else item
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key]= 1 
    return frequencies

dictionary = frequencies([100, 'Hello', '100', '100', 100])
print(dictionary)
