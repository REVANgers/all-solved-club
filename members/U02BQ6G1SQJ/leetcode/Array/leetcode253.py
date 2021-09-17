import heapq;

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        (answer, roomCnt, curTime, pq, intervalList) = (0, 0, 0, [], sorted(intervals));
        
        for (curStart, curEnd) in intervalList:
            curTime = curStart;
            
            # print(curStart, curEnd, curTime);

            while ((pq) and (curTime >= pq[0][0]) and (curEnd >= pq[0][0])):
                heapq.heappop(pq);
                roomCnt -= 1;
                
            heapq.heappush(pq, [curEnd, curStart]);
            roomCnt += 1;
            answer = max(answer, roomCnt);
            
            # print(answer, roomCnt);
            # print(pq);
            
        return answer;
