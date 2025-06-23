class Solution:
    def checkValue(self, i, V):
        if i in V:
            return 1
        return 0

    def maxVowels(self, s: str, k: int) -> int:
        V = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        S = list(s)
        current_num = 0

        for i in range(k):
            current_num += self.checkValue(S[i], V)

        max_num = current_num
        
        for i in range(len(S)-k):
            current_num = current_num - self.checkValue(S[i], V) + self.checkValue(S[i+k], V)
            max_num = max(max_num, current_num)
        
        return max_num
        