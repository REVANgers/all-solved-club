# reference : https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/Python-with-explanation

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        if (list(filter(lambda k : (len(k) > cols), sentence))):
            return 0;
        
        (answer, wordIdx, curR, curC) = (0, 0, 0, 0);
        
        while (curR < rows):
            nextC = curC + len(sentence[wordIdx]) - 1;
            
            print("answer :", answer);
            print("cur :", sentence[wordIdx], curR, curC);
            print();
            
            if (curR != 0) and ((wordIdx, curC) == (0, 0)):
                (jumpCnt, remainder) = divmod(rows, curR);
                (answer, curR) = (answer * jumpCnt, curR * jumpCnt);
                
                # print("jumpCnt :", jumpCnt);
                # print("answer :", answer);
                # print("cur :", sentence[wordIdx], curR, curC);
                # print();
                
                if (remainder == 0):
                    break;
            
            if (nextC < cols):
                curC = nextC;
            else:
                (curR, curC) = (curR + 1, len(sentence[wordIdx]));
                
                if (curR == rows):
                    break;
                
            if (curC < cols - 2):
                curC += 2;
            else:
                (curR, curC) = (curR + 1, 0);
                
            if (wordIdx == len(sentence) - 1):
                (answer, wordIdx) = (answer + 1, 0);
                
                if ((curR == 0) and (answer == 1)):
                    (jumpCnt, remainder) = divmod(cols, curC);
                    (answer, curC) = (answer * jumpCnt, curC * jumpCnt);
                    
                    if (remainder == 0):
                        answer *= rows;
                        break;
            else:
                wordIdx += 1;
            
        return answer;
        """
    
        (answer, sentenceStr) = (0, " ".join(sentence) + " ");
        
        for r in range(rows):
            answer += (cols - 1);
            
            if (sentenceStr[answer % len(sentenceStr)] == " "):
                answer += 1;
            elif (sentenceStr[(answer + 1) % len(sentenceStr)] == " "):
                answer += 2;
            else:
                while ((answer > 0) and (sentenceStr[(answer - 1) % len(sentenceStr)] != " ")):
                    answer -= 1;
                    
        return (answer // len(sentenceStr));
