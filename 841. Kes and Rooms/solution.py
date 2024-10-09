from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        available_keys = [0]
        visited_keys = [0]
        while available_keys:
            key = available_keys.pop(0)
            new_keys = rooms[key]
            for new_key in new_keys:
                if new_key not in visited_keys:
                    available_keys.append(new_key)
                    visited_keys.append(new_key)
        # print(locked_rooms)
        # print(visited_keys)
        return len(visited_keys) == len(rooms)

print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(Solution().canVisitAllRooms([[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]))