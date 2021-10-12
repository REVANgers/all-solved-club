class SnapshotArray:
    def __init__(self, length: int):
        self.snapID = 0;
        self.snapIDList = [[] for _ in range(length)];
        self.snapshotList = [{0 : 0} for _ in range(length)];
        
        # print(self.snapID);
        # print(self.snapIDList);
        # print(self.snapshotList);

    def set(self, index: int, val: int) -> None:
        self.snapIDList[index].append(self.snapID);
        self.snapshotList[index][self.snapID] = val;
        
        # print(self.snapID);
        # print(self.snapIDList);
        # print(self.snapshotList);
        
        return None;

    def snap(self) -> int:
        # print(self.snapID);
        # print(self.snapIDList);
        # print(self.snapshotList);
        
        self.snapID += 1;
        return (self.snapID - 1);

    def get(self, index: int, snap_id: int) -> int:
        # print(self.snapID);
        # print(self.snapIDList);
        # print(self.snapshotList);
        
        (targetSnapID, left, right) = (0, 0, len(self.snapIDList[index]) - 1);
        
        while (left <= right):
            mid = (left + right) // 2;
            
            if (snap_id >= self.snapIDList[index][mid]):
                (targetSnapID, left) = (self.snapIDList[index][mid], mid + 1);
            else:
                right = mid - 1;
        
        return (self.snapshotList[index][targetSnapID]);

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
