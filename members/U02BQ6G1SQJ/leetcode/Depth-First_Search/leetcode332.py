beginAirport = "JFK";

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        (answer, s, connectDict) = ([], [beginAirport], dict());
        
        for (src, dst) in tickets:
            connectDict[src] = connectDict.get(src, []) + [dst];

        for connect in connectDict:
            connectDict[connect].sort(reverse = True);

        while (len(s) > 0):
            top = s[-1];

            if ((top in connectDict) and (connectDict[top])):
                s.append(connectDict[top].pop());
            else:
                answer.append(s.pop());

        return answer[ : : -1];
