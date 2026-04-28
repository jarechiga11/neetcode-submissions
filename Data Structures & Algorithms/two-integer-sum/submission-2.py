class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        ## loop thru each index, go thru all other elements until you find one to equal sum (loop)
        ## O(n^2) - Think of a way to only traverse thru array once...

        # Solution: Track the differences
        ## given nums[i] + nums[j] == target, if we rearrange so nums[i] == target - nums[j]
        ## we see that we can check if any previous elements are the matching diff for the target - current.
        ## loop thru each index, get difference (sum - element) and store in HashMap (elem:idx)
        ## each loop, check if diff in hashmap, if yes, return indices

        diffMap = {}
        result = []
        for i,num in enumerate(nums):
            diff = target - num
            if diff in diffMap:
                result = [diffMap[diff], i]
            else:
                diffMap[num] = i
        
        return result
        
        