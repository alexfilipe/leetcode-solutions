from typing import List

class Solution(object):
    def sortedSquares(self, A: List[int]) -> List[int]:
        """Returns sorted squared array of sorted array of integers.

        Args:
            A (List[int]): list of integers.
        Returns:
            List[int]: sorted squared array.
        """
        n = len(A)

        # Starting index of positive values.
        start_positives = 0

        # Find index of starting positive value
        while start_positives < n and A[start_positives] < 0:
            start_positives += 1

        # Divide list into positives and negatives
        negatives = A[:start_positives]
        negatives.reverse() # Reverses list of negatives

        positives = A[start_positives:]

        # Insert items in order into empty array
        sorted_list = []

        # Keep track of positive and negative values
        i_negatives = 0
        i_positives = 0

        # Current positive and negative value
        cur_negative = float('inf')
        cur_positive = float('inf')

        # Loop through all values and add them in order
        while i_negatives < len(negatives) or i_positives < len(positives):

            if i_negatives < len(negatives):
                cur_negative = abs(negatives[i_negatives])
            else:
                cur_negative = float('inf')

            if i_positives < len(positives):
                cur_positive = positives[i_positives]
            else:
                cur_positive = float('inf')

            if cur_negative <= cur_positive:
                sorted_list.append(cur_negative)
                i_negatives += 1

            if cur_positive <= cur_negative:
                sorted_list.append(cur_positive)
                i_positives += 1

        return [k ** 2 for k in sorted_list]
