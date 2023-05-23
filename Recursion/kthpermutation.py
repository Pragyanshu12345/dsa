class Solution:
    def fact(self, n):
        if n == 0:
            return 1
        return n*(self.fact(n-1))

    def solvepermute(self, l, ans, n, k):
        if n == 0:
            return ans
        curr = k//(self.fact(n-1))
        new_k = k % (self.fact(n-1))
        ans += l[curr]
        l.remove(l[curr])
        return self.solvepermute(l, ans, n-1, new_k)

    def get_permutation(self, n: int, k: int) -> str:
        ans = ""
        l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        return self.solvepermute(l, ans, n, k-1)


Sol = Solution()
print(Sol.get_permutation(9, 34445))
