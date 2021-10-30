import copy;

class SparseVector:
    def __init__(self, nums: List[int]):
        self.numList = copy.deepcopy(nums);

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer = 0;
        
        # print(vec);
        
        for numIdx in range(len(self.numList)):
            answer += (self.numList[numIdx] * vec.numList[numIdx]);
            
        return answer;

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
