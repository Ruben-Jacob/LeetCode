class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums1:
            count[num] = count.get(num,0) + 1
        intersection = []
        for num in nums2:
            if num in count and count[num] > 0:
                intersection.append(num)
                count[num] -= 1
        return intersection
                
solution = Solution()
print(solution.intersect([1,2,2,1],[2,2]))
