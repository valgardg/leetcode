class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        s = 0

        def sieve(n, nn):
            #Create a boolean list to track prime status of numbers
            prime = [True] * (n + 1)
            p = 2

            # Sieve of Eratosthenes algorithm
            while p * p <= n:
                if prime[p]:
                    
                    # Mark all multiples of p as non-prime
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1

            # Collect all prime numbers
            res = []
            for p in range(nn if nn > 1 else 2, n + 1):
                if prime[p]:
                    res.append(p)
    
            return res

        print(sieve(max(n, r), min(n, r)))
    
        return sum(sieve(max(n, r), min(n, r)))
