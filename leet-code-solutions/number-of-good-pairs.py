class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counted = Counter(nums)
        result = 0
        
        for key in counted:
            value = counted[key]
            
            result += (value * (value - 1) / 2)
            
        return int(result)
        