from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        remaining = Counter(senate)
        to_ban = {'R': 0, 'D': 0}
        opp = {'R': 'D', 'D': 'R'}
        while remaining['R'] > 0 and remaining['D'] > 0:
            next_s = ""
            for c in senate:
                if to_ban[c] > 0:
                    # c should be banned here
                    print("skipping", c)
                    to_ban[c] -= 1
                    remaining[c] -= 1
                else:
                    # c will ban opposite party
                    print(c, "kills", opp[c])
                    to_ban[opp[c]] += 1
                    next_s += c
            senate = next_s
            
        if remaining['R'] > 0:
            return "Radiant"
        else:
            return "Dire"

            

