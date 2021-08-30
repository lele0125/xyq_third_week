class Solution:
    def combine(self, n, k):
        res=[]
        path = []
        def dfs(startIndex,n,k):
            if len(path)==k:
                res.append(list(path))
                return
            for i in range(startIndex,n+1):
                # if i > n-(k-len(self.path))+1:break
                path.append(i)
                dfs(i+1,n,k)
                path.pop()
        dfs(1,n,k)
        return res