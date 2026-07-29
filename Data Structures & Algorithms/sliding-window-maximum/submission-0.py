class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        left = 0
        result=[]
    
        for right in range(len(nums)):
            
            while dq and nums[dq[-1]]<nums[right]:
                dq.pop()

            dq.append(right)

            while dq and dq[0]<left:
                dq.popleft()

            if right-left+1==k:
                result.append(nums[dq[0]])
                left+=1

        return result

                


            




            
                