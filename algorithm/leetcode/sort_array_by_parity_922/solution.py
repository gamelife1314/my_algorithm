class Solution:

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        length = len(A)
        result = [None] * length
        i, j = 0, 1
        for num in A:
            if num % 2:
                result[j] = num
                j += 2
            else:
                result[i] = num
                i += 2

        return result
