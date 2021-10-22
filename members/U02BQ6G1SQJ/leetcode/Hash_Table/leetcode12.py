VAL_DICT = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"};
VAL_LIST = [1000, 500, 100, 50, 10, 5, 1];
REPLACE_DICT = {"IIII" : "IV", "VIIII" : "IX", "XXXX" : "XL", "LXXXX" : "XC", "CCCC" : "CD", "DCCCC" : "CM"};
REPLACE_LIST = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"];

class Solution:
    def intToRoman(self, num: int) -> str:
        (answer, valIdx) = ("", 0);
        
        while (num > 0):
            (symbolCnt, num) = divmod(num, VAL_LIST[valIdx]);
            (answer, valIdx) = (answer + (VAL_DICT[VAL_LIST[valIdx]] * symbolCnt), valIdx + 1);
            
        for replaceKey in REPLACE_LIST:
            answer = answer.replace(replaceKey, REPLACE_DICT[replaceKey]);
            
        # print(answer);
        
        return answer;
