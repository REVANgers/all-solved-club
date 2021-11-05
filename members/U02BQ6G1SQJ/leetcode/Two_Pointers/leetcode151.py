class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join([k for k in s.split(" ") if k][ : : -1]));
