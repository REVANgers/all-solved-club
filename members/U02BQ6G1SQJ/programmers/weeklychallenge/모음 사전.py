import itertools;

MAX_WORD_LEN = 5;
VOWEL_LIST = ["A", "E", "I", "O", "U"];

def solution(word):
    wordList = [];
    
    for r in range(1, MAX_WORD_LEN + 1):
        wordList.extend(["".join(k) for k in itertools.product(VOWEL_LIST, repeat = r)]);
            
    # print(wordList);
    
    return (sorted(wordList).index(word) + 1);
