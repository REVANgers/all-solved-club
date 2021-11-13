import collections;

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        (bulls, cows, secretCounter, guessCounter) = (0, len(secret), collections.Counter(secret), collections.Counter(guess));
        diffCounter = secretCounter - guessCounter;
        
        # print(secretCounter);
        # print(guessCounter);
        # print(diffCounter);
        
        for secretIdx in range(len(secret)):
            if (secret[secretIdx] == guess[secretIdx]):
                (bulls, cows) = (bulls + 1, cows - 1);
                
        for val in diffCounter.values():
            cows -= val;
                
        return ("%dA%dB" % (bulls, cows));
