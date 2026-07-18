class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        seen = set()
        result = []

        def can_form(word):
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in seen:
                        dp[i] = True
                        break
            return dp[n]
        for word in words:
            if word and can_form(word):
                result.append(word)

            seen.add(word)

        return result