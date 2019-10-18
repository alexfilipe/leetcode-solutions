class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
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

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        remainder = num
        divisions = dict()

        roman = ""

        for v in values:
            division = remainder // v
            remainder = remainder % v

            divisions[v] = division

            if divisions[v] != 0:
                roman += symbols[v] * divisions[v]

        return roman
