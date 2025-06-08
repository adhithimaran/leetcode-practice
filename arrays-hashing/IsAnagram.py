def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        # check equality of strings
        if (sorted_s == sorted_t):
            return True
        else:
            return False