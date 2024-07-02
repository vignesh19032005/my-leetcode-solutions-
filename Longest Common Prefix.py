class Solution:
    def longestCommonPrefix(self,strs):
        s = ""
        l = len(min(strs, key=len))
        strs.sort()
        for i in range(l):
            if strs[0][i] == strs[-1][i]:
                s += strs[0][i]
            else:
                break
        return s
s=Solution()
strs=["flower","flowflow","flight"]
print(s.longestCommonPrefix(strs))
