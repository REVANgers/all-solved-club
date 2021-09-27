def solution(sizes):
    (minList, maxList) = ([], []);
    
    for (width, height) in sizes:
        minList.append(min(width, height));
        maxList.append(max(width, height));
    
    return (max(minList) * max(maxList));
