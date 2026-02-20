from collections import defaultdict
class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_y = 0
        current_y = 0
        x_history = defaultdict(list)
        special_strings = []
        values = []

        for i, c in enumerate(s):
            print(f'{i}({c}): last_y: {last_y}, current_y: {current_y}, x_history: {x_history}')

            if c == "0" and i < len(s) - 1 and s[i+1] == "1":
                print(f"special string")
                special_cords = [x_history[current_y-1][-1], i + 1]
                special_strings.append(special_cords)
                last_y = current_y - 1
                values.append(int(s[special_cords[0]:special_cords[1]], 2))

            elif c == "0" and i < len(s) - 1 and s[i+1] == "0" and current_y - 1 == last_y:
                print(f"special string")
                special_cords = [x_history[current_y-1][-1], i + 1]
                special_strings.append(special_cords)
                last_y = current_y - 1
                values.append(int(s[special_cords[0]:special_cords[1]], 2))

            x_history[current_y].append(i)
            current_y += 1 if c == "1" else -1

        indexes = dict()
        for i, string in enumerate(special_strings):
            indexes[tuple(string)] = i

        print(special_strings)
        print(indexes)
        print(values)

        sorted_special_strings = sorted(special_strings, key=lambda cord: int(s[cord[0]:cord[1]], 2), reverse=True)
        print(sorted_special_strings)

        return s
            
        

        

print(Solution().makeLargestSpecial("11011000"))
# print(Solution().makeLargestSpecial("10"))
