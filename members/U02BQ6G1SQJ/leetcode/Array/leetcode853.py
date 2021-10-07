# reference : https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward
# import collections;
# import heapq;

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        (answer, positionDict) = (0, collections.defaultdict(set));
        
        for carIdx in range(len(position)):
            positionDict[position[carIdx]].add(carIdx);
        
        while (True):
            isFinished = True;
            
            for carIdx in range(len(position)):
                if (position[carIdx] == target):
                    continue;
                    
                isFinished = False;
                positionDict[position[carIdx]].remove(carIdx);
                position[carIdx] = min(target, position[carIdx] + speed[carIdx]);
                positionDict[position[carIdx]].add(carIdx);

            if (isFinished):
                break;
                
            for (key, val) in positionDict.items():
                if (not val):
                    continue;

                if (key == target):
                    answer += 1;
                    val.clear();
                    continue;
                    
                minSpeed = min([speed[k] for k in val]);

                for carIdx in val:
                    speed[carIdx] = minSpeed;

            # print(positionDict);
            # print(speed);
            # print();
                
        return answer;
        """
        
        """
        (answer, pq) = (0, [[-k[0], k[1]] for k in zip(position, speed)]);
        heapq.heapify(pq);
        
        # print(pq);
        
        while (True):
            (minHeap, maxHeap) = ([], []);

            while (pq):
                (curPosition, curSpeed) = heapq.heappop(pq);
                nextPosition = curPosition - curSpeed;
                
                if ((minHeap) and (-nextPosition >= minHeap[0][0])):
                    continue;

                heapq.heappush(minHeap, [-nextPosition, curSpeed]);
                heapq.heappush(maxHeap, [nextPosition, curSpeed]);

            print(answer);
            print(minHeap);
            print(maxHeap);
            print();
            
            while (maxHeap):
                (nextPosition, nextSpeed) = maxHeap[0];
                
                if (nextPosition <= -target):
                    answer += 1;
                    heapq.heappop(maxHeap);
                else:
                    break;
                
            if (not maxHeap):
                break;
            elif (len(maxHeap) == 1):
                answer += 1;
                break;
                
            pq = maxHeap;
                
        return answer;
        """
        
        (answer, time, arriveTimeList) = (0, 0, [(float(target - p) / s) for (p, s) in sorted(zip(position, speed), key = lambda k : (-k[0], -k[1]))]);
        
        for curArriveTime in arriveTimeList:
            if (time < curArriveTime):
                (answer, time) = (answer + 1, curArriveTime);
                
        return answer;
