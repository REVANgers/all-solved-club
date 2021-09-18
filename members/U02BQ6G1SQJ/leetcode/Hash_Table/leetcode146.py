class LinkNode:
    def __init__(self, key : int, value : int, prevNode = None, nextNode = None):
        self.key = key;
        self.value = value;
        self.prevNode = prevNode;
        self.nextNode = nextNode;
        
    def insert(self, cacheDict : dict, key : int, value : int) -> None:
        insertNode = LinkNode(key, value, self, self.nextNode);
        (cacheDict[key], self.nextNode.prevNode, self.nextNode) = (insertNode, insertNode, insertNode);
        return None;
        
    def delete(self, cacheDict : dict) -> None:
        (self.prevNode.nextNode, self.nextNode.prevNode) = (self.nextNode, self.prevNode);
        del cacheDict[self.key];
        del self;
        return None;
    
    def printLinkNode(self) -> None:
        print("key :", self.key);
        print("value :", self.value);
        
        if (self.prevNode):
            print("prevNode :", self.prevNode.key);
            
        if (self.nextNode):
            print("nextNode :", self.nextNode.key);
            
        print();
        return None;

class LRUCache:
    def __init__(self, capacity : int):
        self.capacity = capacity;
        self.cacheDict = dict();
        self.head = LinkNode(-1, -1, None, None);
        self.tail = LinkNode(-1, -1, None, None);
        
        (self.head.nextNode, self.tail.prevNode) = (self.tail, self.head);

    def get(self, key : int) -> int:
        if (key not in self.cacheDict.keys()):
            return -1;
        
        value = self.cacheDict[key].value;
        self.cacheDict[key].delete(self.cacheDict);
        self.tail.prevNode.insert(self.cacheDict, key, value);
        
        # print("get ", key);
        # print(self.cacheDict);
        # print("head");
        # self.head.printLinkNode();
        # print("tail");
        # self.tail.printLinkNode();
        
        return self.cacheDict[key].value;

    def put(self, key : int, value : int) -> None:
        if (key in self.cacheDict.keys()):
            self.cacheDict[key].delete(self.cacheDict);
            
        elif (len(self.cacheDict) == self.capacity):
            self.head.nextNode.delete(self.cacheDict);
            
        self.tail.prevNode.insert(self.cacheDict, key, value);
        
        # print("put ", key, value);
        # print(self.cacheDict);
        # print("head");
        # self.head.printLinkNode();
        # print("tail");
        # self.tail.printLinkNode();
        
        return None;
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
