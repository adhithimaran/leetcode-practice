def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # copy of list but each word in alphabetical order (reordered)
        # group all same alpha elements from copy list into new list and append to output
        output = []
        reordered_words = []
        for i in range(len(strs)):
            word = sorted(list(strs[i]))
            word = ''.join(word)
            reordered_words.append(word)
        ana = {}
        for i in range(len(reordered_words)):
            if reordered_words[i] in ana:
                ana[reordered_words[i]].append(strs[i])
            else:
                ana[reordered_words[i]] = [strs[i]]
        for value in ana.values():
            output.append(value)
        return output

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))