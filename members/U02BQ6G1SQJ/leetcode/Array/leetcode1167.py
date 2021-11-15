import heapq;

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        answer = 0;
        heapq.heapify(sticks);
        
        # print(sticks);
        
        while (len(sticks) >= 2):
            curCost = heapq.heappop(sticks) + heapq.heappop(sticks);
            answer += curCost;
            heapq.heappush(sticks, curCost);
            
        return answer;
