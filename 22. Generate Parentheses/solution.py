from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left_count = n
        right_count = n

        ans = self.dig(left_count, right_count, "")
        return ans

    def dig(self, left_count, right_count, generated):
        answer = []
        if left_count == 0 and right_count == 0:
            return [generated]
        if left_count == right_count: # "()"
            answer.extend(self.dig(left_count - 1, right_count, generated + "("))
        if left_count < right_count: # "(()"
            if left_count > 0: answer.extend(self.dig(left_count - 1, right_count, generated + "("))
            answer.extend(self.dig(left_count, right_count - 1, generated + ")"))

        return answer


    
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))