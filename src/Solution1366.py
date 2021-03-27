class Solution:
    def rankTeams(self, votes: [str]) -> str:
        if len(votes) < 0:return ''
        rankTeam, teamRank = {}, {}
        for i in range(len(votes)):
            for j, vt in enumerate(votes[i]):
                if j not in rankTeam:
                    rankTeam[j] = [vt]
                else:
                    rankTeam[j].append(vt)
                if vt not in teamRank:
                    teamRank[vt] = [j]
                else:
                    teamRank[vt].append(j)
        rankTeam = dict(sorted(rankTeam.items(), key=lambda kv: kv[0]))
        teamRank = dict(sorted(teamRank.items(), key=lambda kv: kv[1]))
        ans = ''
        for key in rankTeam:
            td = {}
            for t in rankTeam[key]:
                if t not in td:
                    td[t] = 1
                else:
                    td[t] += 1
            td = sorted(td.items(), key=lambda kv:kv[1],reverse=True)
            ans += td[0][0]
        print(rankTeam)
        print(teamRank)
        return ans

votes = ["ABC","ACB","ABC","ACB","ACB"]
votes = ["WXYZ","XYZW"]
sol = Solution()
res = sol.rankTeams(votes)
print(res)

