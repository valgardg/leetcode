class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]
            if schar in ds:
                ds[schar] += 1
            else:
                ds[schar] = 1

            if tchar in dt:
                dt[tchar] += 1
            else:
                dt[tchar] = 1

        for key in ds.keys():
            if key not in dt:
                return False
            if dt[key] != ds[key]:
                return False
        return True