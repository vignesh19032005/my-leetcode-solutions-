class Solution:
    def addTwoNumbers(self, l1,l2):
        a=""
        b=""

        for i in l1:
            a+=str(i)
        for j in l2:
            b+=str(j)

        d=a[::-1]
        e=b[::-1]
        c=int(d)+int(e)
        f=str(c)[::-1]

        aa=[*f]
        bb=[]
        for i in aa:
            j=int(i)
            bb.append(j)

        print(bb)

l1,l2=[2,4,3],[5,6,4]
s=Solution()
s.addTwoNumbers(l1,l2)
