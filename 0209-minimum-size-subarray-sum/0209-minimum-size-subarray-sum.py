class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 1
        currlen = 0
        minlen = len(nums)
        currsum = sum(nums[l:r])

        while(True):
            if currsum < target:
                if (r < len(nums)):
                    currsum = currsum + nums[r]
                    r+=1
                else:
                    l-=1
                    break
            else:
                currlen = len(nums[l:r])
                minlen = min(minlen, currlen)
                currsum = currsum - nums[l]
                l+=1
                
        if (l==-1):
            return 0
        else:
            return(minlen)