import itertools;

LETTER_LIST = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (not digits):
            return [];
        
        productList = list(itertools.product(*[LETTER_LIST[int(k)] for k in digits]));
        return ["".join(k) for k in productList];
