#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    roman_string: The Roman numeral to be converted.

    Returns: The equivalent integer value.
    """
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not (roman_string and isinstance(roman_string, str)):
        return 0

    int_value = romans[roman_string[-1]]
    for i in range(len(roman_string) - 1, 0, -1):
        current_value = romans[roman_string[i]]
        previous_value = romans[roman_string[i - 1]]

        if previous_value >= current_value:
            int_value += previous_value
        else:
            int_value -= previous_value
    return int_value
