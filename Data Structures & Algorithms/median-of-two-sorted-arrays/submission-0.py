class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        half = (len(nums1)+len(nums2)+1) // 2
        left = 0
        right = len(nums1)

        while left <= right:

            part1 = (left+right)//2
            part2 = half - part1
            left1=nums1[part1-1] if part1 > 0 else float('-inf')
            right1 = nums1[part1] if part1 < len(nums1) else float('inf')
            left2 = nums2[part2-1] if part2 > 0 else float('-inf')
            right2 = nums2[part2] if part2 < len(nums2) else float('inf')

            if left1 <= right2 and left2 <= right1:

                if (len(nums2) + len(nums1)) % 2:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                right = part1 - 1

            else:
                left = part1 + 1

    

    
