"""
Multiply each item in list by its place value and add it all up.
"""

def ListtoInt(lst):
    result = 0            # Initialise an integer variable to store result
    length = len(lst) - 1 # Calculates the place value position (Starts from the first digit)
    for num in lst:       # Loop over each number in list
        result += num * (10**length) # Multiply the number with it's place value
        length -= 1
    return result

lst = [8,3,5,1]
print(ListtoInt(lst))