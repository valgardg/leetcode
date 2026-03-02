class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """

        current_key = ""
        add_to_key = False

        knowledge_dict = {}
        for key, value in knowledge:
            knowledge_dict[key] = value

        for c in s:
            if add_to_key and c != ")":
                current_key += c
            elif c == "(":
                add_to_key = True
            elif c == ")":
                add_to_key = False
                replace_string = "(" +  current_key + ")"
                if current_key in knowledge_dict:
                    s = s.replace(replace_string, knowledge_dict[current_key])
                else:
                    s = s.replace(replace_string, '?')
                current_key = ""
        return s
