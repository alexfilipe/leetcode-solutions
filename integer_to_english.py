class Solution:
    def __init__(self):
        self.integers = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        self.dozens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

    def zeroToHundred(self, num: int) -> str:
        if 0 <= num < 20:
            return self.integers[num]
        elif 20 <= num < 100:
            dozen = (num // 10) * 10
            unit = num % 10

            if unit > 0:
                return "{} {}".format(
                    self.dozens[dozen],
                    self.integers[unit]
                )
            else:
                return self.dozens[dozen]
        else:
            return ""

    def hundredToThousand(self, num: int) -> str:
        if 100 <= num < 1000:
            hundreds = num // 100
            remainder = num % 100

            if remainder > 0:
                return "{} Hundred {}".format(
                    self.integers[hundreds],
                    self.zeroToHundred(remainder)
                )
            else:
                return "{} Hundred".format(self.integers[hundreds])

        else:
            return ""

    def thousandToMillion(self, num: int) -> str:
        if 1000 <= num < 1000000:
            thousands = num // 1000
            thousand_str = ""

            if 1 <= thousands < 100:
                thousand_str = "{} Thousand".format(self.zeroToHundred(thousands))
            elif 100 <= thousands < 1000:
                thousand_str = "{} Thousand".format(self.hundredToThousand(thousands))

            remainder = num % 1000

            if remainder > 0:
                remainder_str = ""

                if 1 <= remainder < 100:
                    remainder_str = self.zeroToHundred(remainder)
                elif 100 <= remainder < 1000:
                    remainder_str = self.hundredToThousand(remainder)

                return "{} {}".format(thousand_str, remainder_str)
            else:
                return thousand_str
        else:
            return ""

    def millionToBillion(self, num: int) -> str:
        if 1000000 <= num < 1000000000:
            millions = num // 1000000
            million_str = ""

            if 1 <= millions < 100:
                million_str = "{} Million".format(self.zeroToHundred(millions))
            else:
                million_str = "{} Million".format(self.hundredToThousand(millions))

            remainder = num % 1000000

            if remainder > 0:
                remainder_str = ""

                if 1 <= remainder < 100:
                    remainder_str = self.zeroToHundred(remainder)
                elif 100 <= remainder < 1000:
                    remainder_str = self.hundredToThousand(remainder)
                elif 1000 <= remainder < 1000000:
                    remainder_str = self.thousandToMillion(remainder)

                return "{} {}".format(million_str, remainder_str)
            else:
                return million_str
        else:
            return ""

    def billionToInfinity(self, num: int) -> str:
        if 1000000000 <= num:
            billions = num // 1000000000
            billion_str = ""

            if 1 <= billions < 100:
                billion_str = "{} Billion".format(self.zeroToHundred(billions))
            else:
                billion_str = "{} Billion".format(self.hundredToThousand(billions))

            remainder = num % 1000000000

            if remainder > 0:
                remainder_str = ""

                if 1 <= remainder < 100:
                    remainder_str = self.zeroToHundred(remainder)
                elif 100 <= remainder < 1000:
                    remainder_str = self.hundredToThousand(remainder)
                elif 1000 <= remainder < 1000000:
                    remainder_str = self.thousandToMillion(remainder)
                elif 1000000 <= remainder < 1000000000:
                    remainder_str = self.millionToBillion(remainder)

                return "{} {}".format(billion_str, remainder_str)
            else:
                return billion_str
        else:
            return ""

    def numberToWords(self, num: int) -> str:
        if 0 <= num < 100:
            return self.zeroToHundred(num)
        elif 100 <= num < 1000:
            return self.hundredToThousand(num)
        elif 1000 <= num < 1000000:
            return self.thousandToMillion(num)
        elif 1000000 <= num < 1000000000:
            return self.millionToBillion(num)
        else:
            return self.billionToInfinity(num)
