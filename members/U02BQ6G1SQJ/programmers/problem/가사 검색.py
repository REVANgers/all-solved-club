import sys;

MAX_WORDS_LEN = 100000;

class TrieNode:
    def __init__(self, key = "", data = "", count = 0, childDict = dict()):
        self.key = key;
        self.data = data;
        self.count = count;
        self.childDict = childDict;
        
    def printTrieNode(self):
        print("key :", self.key);
        print("data :", self.data);
        print("count :", self.count);
        print("childDict :", self.childDict);
        return None;

def addTrieNode(curNode : TrieNode, curWord : str, depth : int) -> None:
    # curNode.printTrieNode();
    # print(curWord, depth);
    # print();
    
    curNode.count += 1;
    
    if (depth == len(curWord)):
        curNode.data = curWord;
        
        # curNode.printTrieNode();
        # print(curWord, depth);
        # print();
        
        return None;
    
    curCh = curWord[depth];
    
    if (curCh not in curNode.childDict.keys()):
        curNode.childDict[curCh] = TrieNode(curCh, "", 0, dict());
        
    addTrieNode(curNode.childDict[curCh], curWord, depth + 1);
    return None;
    
def queryTrieNode(curNode : TrieNode, curQuery : str, depth : int) -> int:
    # curNode.printTrieNode();
    # print(curQuery, depth);
    # print();
    
    if (depth == len(curQuery)):
        return 1;
    
    curCh = curQuery[depth];
    
    if (curCh == "?"):
        # curNode.printTrieNode();
        # print(curQuery, depth);
        # print();
        
        return curNode.count;
    elif (curCh not in curNode.childDict.keys()):
        # curNode.printTrieNode();
        # print(curQuery, depth);
        # print();
        
        return 0;
    
    return queryTrieNode(curNode.childDict[curCh], curQuery, depth + 1);
    
def solution(words : list, queries : list) -> list:
    sys.setrecursionlimit(MAX_WORDS_LEN);
    (answerList, answerDict) = ([], dict());
    (prefixRootList, suffixRootList) = ([TrieNode("", "", 0, dict()) for _ in range(MAX_WORDS_LEN + 1)], [TrieNode("", "", 0, dict()) for _ in range(MAX_WORDS_LEN + 1)]);
    
    for curWord in words:
        # print(curWord, curWord[ : : -1]);
        
        addTrieNode(prefixRootList[len(curWord)], curWord, 0);
        addTrieNode(suffixRootList[len(curWord)], curWord[ : : -1], 0);
        
    # prefixRoot.printTrieNode();
    # suffixRoot.printTrieNode();
    
    for curQuery in queries:
        # print(answerDict);
        
        if (curQuery in answerDict.keys()):
            answerList.append(answerDict[curQuery]);
        else:
            queryResult = (queryTrieNode(prefixRootList[len(curQuery)], curQuery, 0) if (curQuery.endswith("?")) else (queryTrieNode(suffixRootList[len(curQuery)], curQuery[ : : -1], 0)));
            answerList.append(queryResult);
            answerDict[curQuery] = queryResult;
    
    return answerList;
