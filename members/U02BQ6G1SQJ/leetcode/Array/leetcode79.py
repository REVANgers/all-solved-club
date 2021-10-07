import collections;

DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

def checkImpossible(boardList : List[List[str]], wordStr : str, r : int, c : int, curStr : str, curSet : set):
    return ((r < 0) or (r >= len(boardList)) or (c < 0) or (c >= len(boardList[r])) or (tuple([r, c]) in curSet) or (len(curStr) >= len(wordStr)) or (boardList[r][c] != wordStr[len(curStr)]));

def bfs(boardList : List[List[str]], wordStr : str, startR : int, startC : int):
    dq = collections.deque([[startR, startC, wordStr[0], set([tuple([startR, startC])])]]);
    
    while (dq):
        (curR, curC, curStr, curSet) = dq.popleft();
        
        # print("curR :", curR);
        # print("curC :", curC);
        # print("curStr :", curStr);
        # print("curSet :", curSet);
        # print();
        
        if (curStr == wordStr):
            return True;
        
        for (dr, dc) in DIR_VEC:
            (nextR, nextC) = (curR + dr, curC + dc);
            
            if checkImpossible(boardList, wordStr, nextR, nextC, curStr, curSet):
                continue;
                
            dq.append([nextR, nextC, curStr + boardList[nextR][nextC], curSet | set([tuple([nextR, nextC])])]);
        
    return False;

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        (boardCounter, wordCounter) = (collections.Counter(), collections.Counter(word));
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                boardCounter[board[r][c]] += 1;
                
        # print(boardCounter);
        # print(wordCounter);
        # print(wordCounter - boardCounter);
        
        if (wordCounter - boardCounter):
            return False;
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if ((board[r][c] == word[0]) and (bfs(board, word, r, c))):
                    return True;
                
        return False;
