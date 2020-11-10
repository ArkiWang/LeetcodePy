class Solution:
    def check(self, num: str, word: str) -> bool:
        alphabet = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        if len(num) != len(word): return False
        for i in range(len(num)):
            if word[i] not in alphabet.get(num[i]):
                return False
        return True
    def getValidT9Words(self, num: str, words: [str]) -> [str]:
        #abc def ghi jkl mno pqrs tuv wxyz
        res = []
        for w in words:
            if self.check(num, w):
                res.append(w)
        return res
