import random
import string
import text_formatting

# Operation type constants to improve readability
ARRANGE_ASCENDINGLY = 0
ARRANGE_DESCENDINGLY = 1
CAPITALIZE = 2

# This function takes a string and returns a new string with all the characters in uppercase
def capitalize_all( s: str ) -> str:
    return s.upper()

# This function takes a string a returns a new string with all the characters arranged in ascending order
def arrange_ascendingly( s: str ) -> str:
    return ''.join( sorted(s) )

# This function takes a string a returns a new string with all the characters arranged in descending order
def arrange_descendingly( s: str ) -> str:
    return ''.join( sorted(s, reverse=True) )

"""
This function takes the first character in the string and returns the corresponding operation type
@param c: The first character in the string received from the client
@return: Integer value indicating operation type, or None if the character is not recognized
"""
def get_operation_type( c: str ) -> int or None:
    if c.upper() == 'A':
        return ARRANGE_ASCENDINGLY, text_formatting.set_foreground_color(text_formatting.COLOR_GREEN) + 'ARRANGE ASCENDINGLY' + text_formatting.reset_formatting()

    if c.upper() == 'D':
        return ARRANGE_DESCENDINGLY, text_formatting.set_foreground_color(text_formatting.COLOR_GREEN) + 'ARRANGE DESCENDINGLY' + text_formatting.reset_formatting()
    
    if c.upper() == 'C':
        return CAPITALIZE, text_formatting.set_foreground_color(text_formatting.COLOR_GREEN) + 'CAPITALIZE ALL' + text_formatting.reset_formatting()
    
    return None, text_formatting.set_foreground_color(text_formatting.COLOR_GREY) + 'NONE' + text_formatting.reset_formatting()

"""
This function takes a string and returns a new string with the first character removed and the remaining characters processed
@param s: The string received from the client
@return: The processed string
"""
def process_string( s: str ) -> str:
    # Get the first character and remove it from the string
    op, s = s[0], s[1:]

    # Get the operation type
    op_type, op_name = get_operation_type( op )
    
    # If the operation type is not recognized, return the original string
    if op_type is None: return s
    
    # If the operation type is recognized, process the string and return it
    if op_type is ARRANGE_ASCENDINGLY:
        return arrange_ascendingly(s)
    if op_type is ARRANGE_DESCENDINGLY:
        return arrange_descendingly(s)
    if op_type is CAPITALIZE:
        return capitalize_all(s)

# This function generates a random string of the specified length with the first character more likely to correspond to an operation type
def random_string( length: int ) -> str:
    char_population = ["c", "d", "a", "t", "s", "r", "i", "n"]
    weights = [0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25]
    random_character = random.choices(char_population, weights, k=1)[0]
    letters = string.ascii_lowercase
    return random_character + ''.join(random.choice(letters) for i in range(length - 1))
    