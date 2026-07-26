class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j=len(heights)-1
        maximum=0
        i=0
        while i<j:
            maximum = max(maximum, min(heights[i],heights[j])*(j-i))
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            

        return maximum

            

