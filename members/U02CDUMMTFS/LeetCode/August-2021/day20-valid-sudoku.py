class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            check_list = [0] * 9
            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if check_list[num - 1]:
                        return False
                    check_list[num - 1] += 1
        # column
        for j in range(9):
            check_list = [0] * 9
            for i in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if check_list[num - 1]:
                        return False
                    check_list[num - 1] += 1
        # 3x3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check_list = [0] * 9
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l].isdigit():
                            num = int(board[k][l])
                            if check_list[num - 1]:
                                return False
                            check_list[num - 1] += 1
        return True
