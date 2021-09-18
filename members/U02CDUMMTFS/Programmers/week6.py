def solution(weights, head2head):
    n = len(weights)
    boxers = []
    for i in range(n):
        win = 0
        lose = 0
        fat_win = 0
        for j in range(n):
            if head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    fat_win += 1
            elif head2head[i][j] == 'L':
                lose += 1
        win_rate = 0
        if win:
            win_rate = win / (win + lose)
        boxers.append((win_rate, fat_win, weights[i], i+1))
    boxers.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = list(zip(*boxers))[3]
    return answer
