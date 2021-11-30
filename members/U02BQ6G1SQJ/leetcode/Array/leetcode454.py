import collections;
import itertools;

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        (answer, counter1, counter2, counter3, counter4) = (0, collections.Counter(nums1), collections.Counter(nums2), collections.Counter(nums3), collections.Counter(nums4));
        
        # print(counter1);
        # print(counter2);
        # print(counter3);
        # print(counter4);
        
        for p in itertools.product(counter1.keys(), counter2.keys(), counter3.keys(), counter4.keys()):
            # print(p);
            
            (key1, key2, key3, key4) = p;
            
            if (sum(p) == 0):
                answer += (counter1[key1] * counter2[key2] * counter3[key3] * counter4[key4]);
                
        return answer;
        """
        
        (answer, numCounter) = (0, collections.Counter());
        
        for p12 in itertools.product(nums1, nums2):
            # print(p12);
            
            numCounter[sum(p12)] += 1;
            
        # print(numCounter);
            
        for p34 in itertools.product(nums3, nums4):
            # print(p34);
            
            if (-sum(p34) in numCounter.keys()):
                answer += numCounter[-sum(p34)];
                
        return answer;
