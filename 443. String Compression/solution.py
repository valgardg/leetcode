from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        ichar = chars[0]
        count = 1
        index = 0

        for i in range(1, len(chars)):
            if ichar == chars[i]:
                count +=1 
            else:
                chars[index] = ichar
                index += 1
                if count > 1:
                    for char in str(count):
                        chars[index] = char
                        index += 1
                
                ichar = chars[i]
                count = 1
        chars[index] = ichar
        index += 1
        if count > 1:
            for char in str(count):
                chars[index] = char
                index += 1

        print(f'chars: {chars}\ncount: {index}')

        return index

# print(Solution().compress(["a","b","b","c","c","c"]))
Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# Solution().compress(["a","b","b","b"])
# Solution().compress(["a","a","b","b","c","c","c"])