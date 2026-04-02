class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = set()
        left = 0
        solution = 0

        for right in range(len(s)):
            while s[right] in data:
                data.remove(s[left])
                left+=1
            data.add(s[right])
            solution = max(solution,right-left + 1)
        return solution