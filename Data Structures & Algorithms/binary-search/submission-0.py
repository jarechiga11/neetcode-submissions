class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given its sorted, we can half the search by checking midpoints
        ## can utilize Two Pointers, and depending on midpoint, move L or R

        l = 0
        r = len(nums)

        while r - l > 0:
            if nums[l+((r-l)//2)] == target:
                return l+((r-l)//2)
            elif nums[l+((r-l)//2)] > target:
                r = l+((r-l)//2)
            elif nums[l+((r-l)//2)] < target:
                if l == l+((r-l)//2):
                    return -1
                else:
                    l = l+((r-l)//2)
        
        return -1

    

        