from typing import List
from functools import reduce

class Solution:
    def __init__(self):
        # Map of letters in phone dial
        self.letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }


    def letterCombinations(self, digits: str) -> List[str]:
        """Returns all possible letter combinations of a sequence of numbers in
         a phone dial.

        Args:
            digits (str): digits to dial.
        Returns:
            List[int]: all possible letter combinations.
        """
        num_digits = len(digits)

        if num_digits == 0:
            return []

        # Stores combinations found
        combinations = []

        # List of digits to consider
        digit_list = [int(d) for d in digits]

        # Number of letters for each digit
        num_letters = [len(self.letters[d]) for d in digit_list]

        # Counter for current combination
        counter = [0] * num_digits

        # Number of total combinations possible
        num_combinations = reduce(lambda x, y: x * y, num_letters)

        for _ in range(num_combinations):
            # Add current combination (based on counter)
            combinations.append("".join([
                self.letters[digit_list[i]][c] for i, c in enumerate(counter)]
            ))

            carry = False

            for i in reversed(range(num_digits)):
                # Start at the last digit
                if i == num_digits - 1:
                    if counter[i] < num_letters[i] - 1:
                        counter[i] += 1
                    else:
                        counter[i] = 0
                        # Increase previous digit by 1
                        carry = True
                else:
                    if carry: # Increase current digit
                        counter[i] += 1
                        carry = False

                    if counter[i] == num_letters[i]: # Increase previous digit
                        counter[i] = 0
                        carry = True

        return combinations
