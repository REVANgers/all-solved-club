import collections;

class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeDict = collections.defaultdict(list);

    def set(self, key : str, value : str, timestamp : int) -> None:
        self.timeDict[key].append([value, timestamp]);
        return None;

    def get(self, key : str, timestamp : int) -> str:
        if (not self.timeDict[key]):
            return "";
        
        (answer, left, right) = ("", 0, len(self.timeDict[key]) - 1);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            if (self.timeDict[key][mid][1] <= timestamp):
                (answer, left) = (self.timeDict[key][mid][0], mid + 1);
            else:
                right = mid - 1;
                
        return answer;

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
