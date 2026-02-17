from collections import defaultdict
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        
        top_bins = defaultdict(list)
        bottom_bins = defaultdict(list)
        for i in range(0,64):
            binstring = str(bin(i))[2:]
            if i < 16:
                top_bins[binstring.count("1")].append(i)
            bottom_bins[binstring.count("1")].append(i)
        
        answers = []
        for i in range(turnedOn+1):
            # top_options gets i
            top_options = top_bins[i]
            # bottom_options gets turnedOn - i
            bottom_options = bottom_bins[turnedOn - i]

            for option in top_options:
                for option2 in bottom_options:
                    if option > 11 or option2 > 59:
                        continue
                    answers.append("{}:{:02d}".format(option, option2))

        return answers

print(Solution().readBinaryWatch(9))
