from typing import List

class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # print(f'range is [{t - 3000}, {t}]')

        counter = 0

        for value in self.requests:
            if value >= (t-3000) and value <= t:
                counter += 1
        return counter
recentCoutner = RecentCounter()
print(recentCoutner.ping(1))
print(recentCoutner.ping(100))
print(recentCoutner.ping(3001))
print(recentCoutner.ping(3002))