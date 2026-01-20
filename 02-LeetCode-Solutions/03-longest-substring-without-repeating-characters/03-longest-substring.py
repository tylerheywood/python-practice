class Solution:

# Given a string s, find the length of the longest substring without duplicate characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_score = 0

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            max_score = max(max_score, right - left + 1)
        return max_score

solution = Solution()

solution.lengthOfLongestSubstring("tylerheywood")


