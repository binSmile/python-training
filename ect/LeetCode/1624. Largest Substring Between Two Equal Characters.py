class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        addr = dict.fromkeys(set(s),(-1,0,-1))
        for i in range(len(s)):
            c = addr[s[i]][0]
            if c == -1:
                addr[s[i]] = (i,0,-1)
            else:
                addr[s[i]] = (c,i,i-c-1)
        vmax = -1
        for a in addr:
            if addr[a][2] > vmax:
                vmax = addr[a][2]
        return vmax

S = Solution()

for tc in ['aa','abca','cbzxy']:
    print('---')
    print('case: ' + tc)
    print(S.maxLengthBetweenEqualCharacters(tc))


addr = dict.fromkeys(set(s),(-1,0,-1))
for i in range(len(s)):
    c = addr[s[i]][0]
    if c == -1:
        addr[s[i]] = (i,0,-1)
    else:
        addr[s[i]] = (c,i,i-c-1)
vmax = -1
for a in addr:
    if addr[a][2] > vmax:
        vmax = addr[a][2]
