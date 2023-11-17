class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        soln=[]
        def solve(string,curr_open, concluded):
            if concluded ==n:
                while curr_open>0:
                    string+=")"
                    curr_open-=1
                soln.append(string)
                return
            if curr_open!=0:
                solve(string+")", curr_open-1,concluded )
            solve(string +"(", curr_open+1, concluded+1)
        solve("", 0,0)
        return soln
            