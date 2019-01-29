
class Solution:

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        count1, count2 = {}, {}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1

        result = []
        for num, count in count1.items():
            if num in count2:
                result.extend([num] * min([count, count2[num]]))

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
