class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Return string if number of rows is one (bugfix)
        if numRows == 1:
            return s

        currentRow = 0

        # Stores substrings as traversal occurs
        rows = [""] * numRows

        # Direction zigzag is going
        direction = "down"

        # Traverses entire string
        for currentLetter in s:
            rows[currentRow] += currentLetter

            if currentRow == 0:
                direction = "down"
            if currentRow == numRows - 1:
                direction = "up"

            if direction == "down":
                currentRow += 1
            if direction == "up":
                currentRow -= 1

        # Returns joined substrings
        return "".join(rows)
