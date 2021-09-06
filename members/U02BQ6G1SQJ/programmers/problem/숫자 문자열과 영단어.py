# 소요 시간 : 16분
def solution(s : str) -> int:
    (answerStr, chIdx) = ("", 0);
    
    while (chIdx < len(s)):
        if (s[chIdx].isdigit()):
            answerStr += s[chIdx];
            chIdx += 1;
            continue;
        
        # zero
        if (s[chIdx] == "z"):
            answerStr += "0";
            chIdx += 4;
        # one
        elif (s[chIdx] == "o"):
            answerStr += "1";
            chIdx += 3;
        elif (s[chIdx] == "t"):
            # two
            if (s[chIdx + 1] == "w"):
                answerStr += "2";
                chIdx += 3;
            # three
            elif (s[chIdx + 1] == "h"):
                answerStr += "3";
                chIdx += 5;
        elif (s[chIdx] == "f"):
            # four
            if (s[chIdx + 1] == "o"):
                answerStr += "4";
                chIdx += 4;
            # five
            elif (s[chIdx + 1] == "i"):
                answerStr += "5";
                chIdx += 4;
        elif (s[chIdx] == "s"):
            # six
            if (s[chIdx + 1] == "i"):
                answerStr += "6";
                chIdx += 3;
            # seven
            elif (s[chIdx + 1] == "e"):
                answerStr += "7";
                chIdx += 5;
        # eight
        elif (s[chIdx] == "e"):
            answerStr += "8";
            chIdx += 5;
        # nine
        elif (s[chIdx] == "n"):
            answerStr += "9";
            chIdx += 4;

    return int(answerStr);
