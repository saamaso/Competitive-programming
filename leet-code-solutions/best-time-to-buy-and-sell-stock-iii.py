class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        visited={}
        def dfs(index=0, own=False, times=0):
            if(index, own, times) in visited:
                return visited[(index, own , times)]
            if index>=len(prices):
                return 0
            if own:
                a= dfs(index+1,False, times+1) + prices[index]
                b = dfs(index+1, True, times)
                visited[(index, own, times)] = max(a,b)
                return max(a,b)
            else:
                a, b=0,0 
                if times<2:
                    a= dfs(index+1, True, times) - prices[index]
                b = dfs(index+1, False, times)
                visited[(index, own, times)] = max(a,b)
                return max(a,b)
        return dfs()