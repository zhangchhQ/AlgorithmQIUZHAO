class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        re_dict = {}
        for ss in s:
            uni_ss = ord(ss)
            if uni_ss not in re_dict.keys():
                re_dict[uni_ss] = 1
            else:
                re_dict[uni_ss] += 1
        for tt in t:
            uni_tt = ord(tt)
            if uni_tt not in re_dict.keys():
                return False
            else:
                re_dict[uni_tt] -= 1
        for re in re_dict.values():
            if re != 0:
                return False
        return True