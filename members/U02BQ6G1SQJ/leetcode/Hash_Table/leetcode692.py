import collections;

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return (k for (k, v) in sorted([[k, v] for (k, v) in collections.Counter(words).items()], key = lambda k : (-k[1], k[0]))[ : k]);
