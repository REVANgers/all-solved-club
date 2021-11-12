def addTrieNode(curNode : "TrieNode", word : str, idx : int) -> None:
    curNode.cnt += 1;
    
    if (word[idx] not in curNode.childDict.keys()):
        curNode.childDict[word[idx]] = TrieNode(word[idx], "", 1);
        
    if (idx == len(word) - 1):
        curNode.childDict[word[idx]].word = word;
    else:
        addTrieNode(curNode.childDict[word[idx]], word, idx + 1);
        
    return None;
    
def searchTrieNode(curNode : "TrieNode", word : str, idx : int) -> bool:
    if ((word[idx] != ".") and (word[idx] not in curNode.childDict.keys())):
        return False;
    
    if (idx == len(word) - 1):
        if (word[idx] == "."):
            for nextNode in curNode.childDict.values():
                if (nextNode.word):
                    return True;
        else:
            return curNode.childDict[word[idx]].word;
    else:
        if (word[idx] == "."):
            for nextNode in curNode.childDict.values():
                if (searchTrieNode(nextNode, word, idx + 1)):
                    return True;
        else:
            return searchTrieNode(curNode.childDict[word[idx]], word, idx + 1);
            
    return False;
    
class TrieNode:
    def __init__(self, ch = "", word = "", cnt = 0):
        self.ch = ch;
        self.word = word;
        self.cnt = cnt;
        self.childDict = dict();
        
    def printTrieNode(self) -> None:
        print("ch :", self.ch);
        print("word :", self.word);
        print("cnt :", self.cnt);
        print("childDict :", self.childDict);
        print();
        return None;

class WordDictionary:
    def __init__(self):
        self.root = TrieNode("", "", 0);
        
        # self.root.printTrieNode();

    def addWord(self, word: str) -> None:
        addTrieNode(self.root, word, 0);
        
        # self.root.printTrieNode();
        
        return None;

    def search(self, word: str) -> bool:
        return searchTrieNode(self.root, word, 0);
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
