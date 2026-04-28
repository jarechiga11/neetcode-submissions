class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given its sorted, we can half the search by checking midpoints
        ## can utilize Two Pointers, and depending on midpoint, move L or R

        l = 0
        r = len(nums) - 1

        while l <= r:
            midpoint = l+((r-l)//2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                # since bigger, go down one extra
                r = midpoint - 1
            elif nums[midpoint] < target:
                # since smaller, go up one extra        
                    l = midpoint + 1
        
        return -1

    

        