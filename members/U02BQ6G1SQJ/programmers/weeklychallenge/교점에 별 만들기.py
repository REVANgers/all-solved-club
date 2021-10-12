def solution(line):
    (answerList, intersectionPointSet) = ([], set());
    
    for i in range(len(line)):
        (a, b, e) = line[i];
        
        for j in range(i + 1, len(line)):
            (c, d, f) = line[j];
            
            # print(a, b, c);
            # print(d, e, f);
            # print();
            
            if (a * d == b * c):
                continue;
                
            denominator = (a * d) - (b * c);
            (x, y) = ((((b * f) - (e * d)) / denominator), (((e * c) - (a * f)) / denominator));
            
            if ((x.is_integer()) and (y.is_integer())):    
                intersectionPointSet.add(tuple([int(x), int(y)]));

    intersectionPointList = sorted(list(intersectionPointSet), key = lambda k : (-k[1], k[0]));
    (xList, yList) = zip(*intersectionPointList);
    
    # print(intersectionPointSet);
    # print(intersectionPointList);
    # print(xList);
    # print(yList);
    
    for y in range(max(yList), min(yList) - 1, -1):
        answerStr = "";
        
        for x in range(min(xList), max(xList) + 1):
            # print(x, y);
            
            answerStr += ("*" if ((x, y) in intersectionPointSet) else ".");
            
        answerList.append(answerStr);
        
    return answerList;
