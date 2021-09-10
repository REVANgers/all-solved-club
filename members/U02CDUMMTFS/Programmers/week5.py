def solution(word):
    queue = ['A', 'E', 'I', 'O', 'U']
    candidate = []
    while queue:
        q = queue.pop(0)
        if len(q) < 5:
            for alpha in "AEIOU":
                queue.append(q + alpha)
        candidate.append(q)
    candidate.sort()
    answer = candidate.index(word) + 1
    return answer
