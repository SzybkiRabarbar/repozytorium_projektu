from classes.Roman_Numerals_Helper import RomanNumerals

def is_roman_valid(roman_number:str):
    if not type(roman_number)==str: return False
    roman_number = roman_number.upper()
    for rn in roman_number: 
        if not rn in ['I','V','X','L','C','D','M']: return False
    arabic_number = RomanNumerals.from_roman(roman_number)
    if arabic_number>3999 or roman_number!=RomanNumerals.to_roman(arabic_number):
        return False
    return arabic_number

if __name__ == '__main__':
    roman_number = input("Wprowadź liczbę rzymską (od 1 do 3999): ")
    is_valid = is_roman_valid(roman_number)
    if is_valid:
        print(roman_number.upper(),'jest równe',is_valid)
    else:
        print('Źle wprowadzone dane!')