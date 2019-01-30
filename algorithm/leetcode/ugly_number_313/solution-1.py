import heapq


class Solution:

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_numbers = [1] * n
        hq = [(prime, 1, prime) for prime in primes]
        heapq.heapify(hq)
        for i in range(1, n):
            ugly_numbers[i] = hq[0][0]
            while ugly_numbers[i] == hq[0][0]:
                _, idx, prime = heapq.heappop(hq)
                heapq.heappush(hq, (ugly_numbers[idx] * prime, idx + 1, prime))
        return ugly_numbers[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(10, [2, 3, 5]))
