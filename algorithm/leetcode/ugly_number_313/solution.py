

class Solution:

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        indexes = {prime: 0 for prime in primes}
        ugly_numbers, count = [1] * n, 1
        while count < n:
            min_ugly_number = min([ugly_numbers[indexes[prime]] * prime for prime in primes])
            for prime in primes:
                if min_ugly_number == ugly_numbers[indexes[prime]] * prime:
                    indexes[prime] += 1
                    break
            if min_ugly_number != ugly_numbers[count - 1]:
                ugly_numbers[count] = min_ugly_number
                count += 1
        return ugly_numbers[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(10, [2, 3, 5]))
