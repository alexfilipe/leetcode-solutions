import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        # If number is negative (corner case)
        negative = x < 0

        # Normalize number
        x = abs(x)

        # Number of digits in number
        digits = math.floor(math.log10(x)) + 1

        # Store reversed number
        reverse = 0

        for n in range(1, digits + 1):
            # Portion outside of power of 10
            remainder = x % (10 ** n)

            # Digit in current power of 10
            digit = remainder // (10 ** (n - 1))

            # Digit in correct power of 10 (reverse)
            dozen = digit * (10 ** (digits - n))

            reverse += dozen

        if negative:
            reverse *= -1

        # Return only if in 32 bit range
        if -2 ** 31 <= reverse <= 2 ** 31 - 1:
            return reverse

        return 0
