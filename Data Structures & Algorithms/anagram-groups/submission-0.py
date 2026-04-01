class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        anagram = {}
        output = []
        for word in strs:
            word_sort = ("".join(sorted(word)))
            anagram[word_sort] = []
        for word in strs:
            word_sort = "".join(sorted(word))
            anagram[word_sort].append(word)
        return list(anagram.values())

