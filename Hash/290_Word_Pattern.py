class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        myhash = {}
        str_list = str.split(' ')
        if len(str_list) != len(pattern): return False
        for index, s in enumerate(str_list):
            if s in myhash:
                if myhash[s] != pattern[index]:
                    return False
            else:
                if pattern[index] in myhash.values(): return False
                myhash[s] = pattern[index]
        return True