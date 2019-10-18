class Solution:
    def __init__(self):
        # Symbols representing units of Roman numerals up to 1000.
        self.symbols = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        # Integers representing remainders in Roman numerals up to 1000.
        self.values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def intToRoman(self, num: int) -> str:
        """Returns Roman numeral representation of an integer up to 3999.

        Args:
            num (int): Integer to be converted.
        Returns:
            str: Roman numeral.
        """

        # Last remainder
        remainder = num

        # Dict representing whole numbers of
        divisions = dict.fromkeys(self.values)

        # Initial string
        roman = ""

        # Loops through all remainder values
        for v in self.values:
            division = remainder // v
            remainder = remainder % v

            divisions[v] = division

            # Adds to the string only if division is not empty.
            if divisions[v] != 0:
                roman += self.symbols[v] * divisions[v]

        return roman
