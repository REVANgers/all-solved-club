class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if (len(palindrome) == 1):
            return "";
        
        (left, right, brokenPalindromeList) = (0, len(palindrome) - 1, []);
        
        while (left < right):
            replaceCh = ("b" if (palindrome[left] == "a") else "a");
            brokenPalindromeList.extend([palindrome[ : left] + replaceCh + palindrome[left + 1 : ], palindrome[ : right] + replaceCh + palindrome[right + 1 : ]]);
            (left, right) = (left + 1, right - 1);
            
        # print(brokenPalindromeList);
        
        return sorted(brokenPalindromeList)[0];
