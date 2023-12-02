class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        tuple_ver = []
        
        for i in range(len(nums)):
            tuple_ver.append((nums[i], cost[i]))
        tuple_ver.sort()
        
        forward = [0]
        
        curr_cost = 0
        prefix_sum = 0
        for i in range(1, len(nums)):
            new_sum = (prefix_sum + tuple_ver[i - 1][1]) * (tuple_ver[i][0] - tuple_ver[i - 1][0])
            curr_cost += new_sum
            prefix_sum += tuple_ver[i - 1][1]
            forward.append(curr_cost)
        
        reverse = [0]
        curr_cost = 0
        suffix_sum  = 0
        
        for i in range(len(nums) - 2, -1, -1):
            new_sum = (suffix_sum + tuple_ver[i + 1][1]) * (tuple_ver[i + 1][0] - tuple_ver[i][0])
            curr_cost += new_sum
            reverse.append(curr_cost)
            suffix_sum += tuple_ver[i + 1][1]
        
        reverse.reverse()
        for i in range(len(forward)):
            forward[i] += reverse[i]
            
        return min(forward)