REMOVE_CNT = 2;

def moveDoll(transposedBoard : list, stack : list, targetRow : int) -> None:
    targetCol = -1;
    
    for curCol in range(len(transposedBoard)):
        if (transposedBoard[targetRow][curCol] != 0):
            targetCol = curCol;
            break;
    
    if (targetCol == -1):
        return;
    
    stack.append(transposedBoard[targetRow][targetCol]);
    transposedBoard[targetRow][targetCol] = 0;
    
    # print(transposedBoard);
    # print(stack);
    # print(targetRow, targetCol);
    
    return None;

def checkStack(stack : list) -> int:
    if ((len(stack) < REMOVE_CNT) or (stack[-1] != stack[-2])):
        return 0;
    
    stack.pop();
    stack.pop();
    return REMOVE_CNT;

def solution(board : list, moves : list) -> int:
    answer = 0;
    (stack, transposedBoard) = ([], list(map(list, zip(*board))));
    
    # print(transposedBoard);
    
    for curMove in moves:
        moveDoll(transposedBoard, stack, curMove - 1);
        answer += checkStack(stack);
    
    return answer;
