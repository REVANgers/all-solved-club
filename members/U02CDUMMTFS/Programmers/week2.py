def solution(scores):
    answer = ''
    for idx, score in enumerate(zip(*scores)):
        total = sum(score)
        n = len(score)
        if score[idx] == max(score) or score[idx] == min(score):
            if score.count(score[idx]) == 1:
                total -= score[idx]
                n -= 1
        avg = total / n
        if avg < 50:
            answer += 'F'
        elif avg < 70:
            answer += 'D'
        elif avg < 80:
            answer += 'C'
        elif avg < 90:
            answer += 'B'
        else:
            answer += 'A'
    return answer
