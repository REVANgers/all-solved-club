# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def isCelebrity(personCnt : int, src : int) -> bool:
    for dst in range(personCnt):
        if (src == dst):
            continue;

        (curIndegree, curOutdegree) = (knows(dst, src), knows(src, dst));

        if ((not curIndegree) or (curOutdegree)):
            return False;
        
    return True;

class Solution:
    def findCelebrity(self, n: int) -> int:
        for curPerson in range(n):
            if (isCelebrity(n, curPerson)):
                return curPerson;
        
        return -1;
