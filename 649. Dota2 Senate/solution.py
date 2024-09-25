class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ans = ''

        rs = [] # R senators
        ds = [] # D senators

        direBan = 0
        radiantBan = 0

        for i in range(len(senate)):
            senator = senate[i]
            if senator == 'R':
                rs.append(i)
            else:
                ds.append(i)

        while ans == '':
            for i in range(len(senate)):
                senator = senate[i]
                # handle the R senate
                if senator == 'R':
                    # if senator still has right to vote
                    if i in rs:
                        if direBan > 0:
                            direBan -= 1
                            rs.remove(i)
                        else:
                            if len(ds) == 0:
                                ans = 'Radiant'
                            else:
                                radiantBan += 1
                    # senator cant do anything
                    else:
                        pass
                # handle the D senate
                else:
                    # if senator still has right to vote
                    if i in ds:
                        if radiantBan > 0:
                            radiantBan -= 1
                            ds.remove(i)
                        else:
                            if len(rs) == 0:
                                ans = 'Dire'
                            else:
                                direBan += 1
                    # senator cant do anything
                    else:
                        pass

        return ans

print(Solution().predictPartyVictory('RD'))
print(Solution().predictPartyVictory('RDD'))
print(Solution().predictPartyVictory('DRRDRDRDRDDRDRDR'))