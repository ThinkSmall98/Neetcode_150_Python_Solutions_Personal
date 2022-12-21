# Time: O(log(n)). Fast pointer splits problem in 2 each time (n, n/2, n/4, ...)
# Space: O(1)
class Solution:
    def isHappy(self, n: int) -> int:
        def get_next_num(num):
            sum_num = 0
            while num:
                num, digit = divmod(num, 10) # return tuple of quotient & remainder
                sum_num += digit ** 2
            return sum_num

        slow = n
        fast = get_next_num(n)
        while fast != 1 and slow != fast:
            slow = get_next_num(slow)
            fast = get_next_num(get_next_num(fast))
        return fast == 1


# Exactly like linked list cycle
