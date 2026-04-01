class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            word_sort = ("".join(sorted(word)))
            if word_sort not in anagram:
                anagram[word_sort] = []
            anagram[word_sort].append(word)
        return list(anagram.values())

