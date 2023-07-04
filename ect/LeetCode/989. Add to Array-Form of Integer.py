class Solution:
    def addToArrayForm(self, num, k):
        maplist = map(str,num)
        nextstr = ''.join(maplist)
        nestnum = int(nextstr) + k
        strnum = str(nestnum)
        reslist = list(str(strnum))
        return reslist


S = Solution()
r = S.addToArrayForm([1,2,0,0],34)
print(r)