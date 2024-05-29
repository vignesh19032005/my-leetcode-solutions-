class Solution:
    def addBinary(self,a,b):
        a=bin(int(int(a,2)+int(b,2)))
        a=a.replace('0b',"")
        return a
        