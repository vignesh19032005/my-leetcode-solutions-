class Solution:
    def romanToInt(self, s):
        a=0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in s:
            if i=='I':
                a+=1
            elif i=='V':
                a+=5
            elif i=='X':
                a+=10
            elif i=='L':
                a+=50
            elif i=='C':
                a+=100
            elif i=='D':
                a+=500
            elif i=='M':
                a+=1000
            else:
                pass
        return a

a=Solution()
s="III"
a.romanToInt(s)
            
        