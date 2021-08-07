def subsets(ip: str, op: str):
    if len(ip) == 0:
        print(op)
        return
    op1 = op
    op2 = op
    op2 += ip[0]
    ip = ip[1:]
    subsets(ip, op1)
    subsets(ip, op2)


def perm_wit_spaces(inp, op):
    if len(inp) == 0:
        print(op)
        return

    op1 = op + " " + inp[0]
    op2 = op + inp[0]
    perm_wit_spaces(inp[1:], op1)
    perm_wit_spaces(inp[1:], op2)


def perm_with_case_change(inp: str, op: str):
    if len(inp) == 0:
        print(op)
        return
    op1 = op + inp[0]
    op2 = op + inp[0].upper()
    perm_with_case_change(inp[1:], op1)
    perm_with_case_change(inp[1:], op2)


#
# inp = "ab"
# perm_with_case_change(inp,"")
# op = inp[0]
# inp = inp[1:]
#
# perm_wit_spaces(inp,op)

def superDigit(n, k):
    p = n * k

    ans = super_dig(p=p)

    return ans


def super_dig(p: str) -> str:
    if len(p) == 1:
        print(p)
        return p
    new_p = 0
    for c in p:
        i = int(c)
        new_p += i
    print(new_p)
    return super_dig(str(new_p))


def balanced_pran(n: int, open: int, close: int, output: str):
    if open == 0 and close == 0:
        print(output)
        return

    if open != 0:
        op1 = output + "("
        balanced_pran(n, open - 1, close, op1)

    if open < close:
        op2 = output + ")"
        balanced_pran(n, open, close - 1, op2)


def bit_binary(n: int, op: str, ones: int, zeros: int):
    if n == 0:
        print(op)
        return
    if ones > zeros:
        op1 = op + "1"
        bit_binary(n - 1, op1, ones + 1, zeros)
        op2 = op + "0"
        bit_binary(n - 1, op2, ones, zeros + 1)
    else:
        op3 = op + "1"
        bit_binary(n - 1, op3, ones + 1, zeros)


def perm(inp: str, op: str):
    if len(inp) == 0:
        print(op)

    for i in range(0, len(inp)):
        op1 = op + inp[i]
        new_inp = inp[:i] + inp[i + 1:]
        perm(new_inp, op1)


# perm("ABC","")


def possible_strings(arr: [str], k: int, ans: str):
    if k == 0:
        print(ans)
        return

    for c in arr:
        new_ans = ans + c
        possible_strings(arr, k - 1, new_ans)


def possible_binary_numbers(n: int, ans: str):
    if n == 0:
        if equal_sum(ans):
            print(ans)
            return
        else:
            return
    ans1 = ans + "0"
    ans2 = ans + "1"

    possible_binary_numbers(n - 1, ans1)
    possible_binary_numbers(n - 1, ans2)


def equal_sum(s: str) -> bool:
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        l_str = s[:mid]
        r_str = s[mid:]
        l_sum = 0
        r_sum = 0
        for c in l_str:
            l_sum += int(c)
        for c in r_str:
            r_sum += int(c)
        return l_sum == r_sum
    else:
        mid = int(len(s) / 2)
        l_str = s[:mid]
        r_str = s[mid + 1:]
        l_sum = 0
        r_sum = 0
        for c in l_str:
            l_sum += int(c)
        for c in r_str:
            r_sum += int(c)
        return l_sum == r_sum


def arr_comb(arr: [int], r: int, ans: str):
    if r == 0:
        print(ans)
        return
    for i in range(0, len(arr)):
        new_ans = ans + str(arr[i])
        new_arr = arr[:i] + arr[i + 1:]

        arr_comb(new_arr, r - 1, new_ans)


def inc_sequence(k: int, arr: [int], ans: str):
    if k == 0:
        print(ans)
        return
    if len(arr) == 0 and k != 0:
        return

    for i in range(0, len(arr)):
        new_ans = ans + str(arr[i])
        new_arr = arr[i + 1:]
        inc_sequence(k - 1, new_arr, new_ans)


def triangle_sum(arr: [int]):
    if len(arr) == 1:
        print(arr)
        return

    new_arr = [(arr[i] + arr[i + 1]) for i in range(0, len(arr) - 1)]
    triangle_sum(new_arr)
    print(arr)


def subset_prob(arr: [int], size: int, sum: int, t: [[]]):
    if sum == 0:
        return True
    if size == 0 and sum != 0:
        return False

    if t[size][sum] != -1:
        return t[size][sum]

    if sum >= arr[size - 1]:
        t[size][sum] = subset_prob(arr, size - 1, sum - arr[size - 1], t) or subset_prob(arr, size - 1, sum, t)
        return t[size][sum]
    else:
        t[size][sum] = subset_prob(arr, size - 1, sum, t)
        return t[size][sum]


def arr(size: int, sum: int):
    s = [[-1 for i in range(0, sum + 1)] for j in range(0, size + 1)]

    return s


# print(subset_prob([2,3,5,6,8,10],6,10,arr(6,10)))


def dp_subset(arr: [int], size: int, sum: int):
    t = [[False for i in range(0, sum + 1)] for j in range(0, size + 1)]
    for j in range(0, sum + 1):
        if j == 0:
            t[0][j] = True
        else:
            t[0][j] = False
    for i in range(0, size + 1):
        t[i][0] = True

    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if j >= arr[i - 1]:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[size][sum]


# print(dp_subset([2,3,5,6,8,10],6,10))


def subset_of_arr(arr: [int], size: int, op: [int]):
    if len(arr) == 0:
        print(op)
        return
    op1 = op + [arr[size - 1]]
    op2 = op
    subset_of_arr(arr[:size - 1], size - 1, op1)
    subset_of_arr(arr[:size - 1], size - 1, op2)


# subset_of_arr([1,2,3,4],4,[])
import string

count = 0


def smaller_strings(s: str, n: int, k: int, op: str):
    alpha = list(string.ascii_lowercase)

    if n == 0:
        global count
        if check_palindrome(op):
            count += 1
        return

    for a in range(0, k):
        if op + alpha[a] < s:
            new_op = op + alpha[a]
            smaller_strings(s, n - 1, k, new_op)


def check_palindrome(s: str):
    rev_str = s[::-1]
    if s == rev_str:
        return True
    else:
        return False


def main():
    t = int(input())
    global count
    for case in range(0, t):
        ip = input()
        n = int(ip.split(" ")[0])
        k = int(ip.split(" ")[1])
        s = input()
        smaller_strings(s, n, k, "")
        print(f"Case #{case + 1}: {count}")

        count = 0


def fib_rec(n: int, dp: [int]):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_rec(n - 1, dp) + fib_rec(n - 2, dp)
    print(dp[n], end=" ")
    return dp[n]


def fib_dp(n: int):
    return [-1 for i in range(0, n + 1)]


def dp_fib(n: int):
    dp = [-1 for _ in range(0, n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def dp_factorial(n: int):
    dp = [-1 for _ in range(0, n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]


import sys


def LIS(arr: [int], prev, currpos):
    if currpos == len(arr):
        return 0

    if prev < arr[currpos]:
        taken = 1 + LIS(arr, arr[currpos], currpos + 1)
        not_taken = LIS(arr, arr[currpos], currpos + 1)
        return max(taken, not_taken)
    else:
        return LIS(arr, arr[currpos], currpos + 1)


# print(LIS([0,1,0,3,2,3],-sys.maxsize-1,0))

# min = sys.maxsize
# def sum(arr:[int],s:int):
#     global min
#     if s == 0:
#        return 0
#     if s <0:
#         return -1
#
#     if s>0:
#         for i in range(0,len(arr)):
#             if s>=arr[i]:
#                  new_sum = 1 + sum(arr,s-arr[i])
#                  if new_sum!=min:
#                      min = new_sum
#
#     return min


total = 0


def target_sum(arr: [int], target: int, op: int, dp: []):
    global total
    if len(arr) == 0:
        if op == target:
            return 1
        return 0

    if dp[len(arr)][op] != -sys.maxsize - 1:
        return dp[len(arr)][op]

    op1 = op + arr[0]
    op2 = op - arr[0]
    add = target_sum(arr[1:], target, op1)
    minus = target_sum(arr[1:], target, op2)
    dp[len(arr)][op] = add + minus


longest_sub = ""


def LPS_dp(n):
    return [-1 for i in range(0, n + 1)]


def LPS(s: str, op: str, dp):
    global longest_sub
    if op == op[::-1]:
        if len(op) > len(longest_sub):
            longest_sub = op

    if len(s) == 0:
        return

    op1 = op + s[0]

    LPS(s[1:], op1, dp)
    LPS(s[1:], "", dp)


# inp = "abbccc"
# LPS(inp,"",LPS_dp(len(inp)))
# print(longest_sub)


def knapsack_prob(wt: [int], val: [int], c: int):
    if c == 0 or len(wt) == 0:
        return 0
    if c >= wt[len(wt) - 1]:
        return max(val[len(wt) - 1] + knapsack_prob(wt[:len(wt) - 1], val, c - wt[len(wt) - 1]),
                   knapsack_prob(wt[:len(wt) - 1], val, c))
    else:
        return knapsack_prob(wt[:len(wt) - 1], val, c)


# print(knapsack_prob([2,3,5,12,8,9],[3,5,7,2,6,9],12))


# def kanpsack_dp(wt:[int],val:[int],c:int):


def can_partition(nums: [int]):
    if sum(nums) % 2 == 0:
        return equal_part(nums, sum(nums) / 2)
    else:
        return False


def equal_part(arr: [int], t: int):
    if t == 0:
        return True
    if len(arr) == 0 and t != 0:
        return False
    if t >= arr[0]:
        return equal_part(arr[1:], t - arr[0]) or equal_part(arr[1:], t)
    else:
        return equal_part(arr[1:], t)


# print(can_partition([1,2,3,5]))

def LCS(s1: str, s2: str):
    dp = [[0 in range(0, len(s2) + 1)] for j in range(0, len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]


# print(LCS("abcde","ace"))


def coinChange(val: [], amount: int):
    dp = [sys.maxsize for _ in range(0, amount + 1)]
    dp[0] = 0

    for value in val:
        for i in range(1, amount + 1):
            if i >= value:
                dp[i] = min(dp[i], 1 + dp[i - value])

    if dp[amount] != sys.maxsize:
        return dp[amount]
    else:
        return -1


def min_cost(days: [int], costs: [int], pack_days: [int]):
    number_days = days[len(days) - 1] + 1
    dp = [sys.maxsize for _ in range(0, 366)]
    dp[0] = 0

    for (index, day) in enumerate(pack_days):
        for i in range(1, 366):
            if i >= day:
                dp[i] = min(dp[i], costs[index] + dp[i - day])

    return dp[max(days)]


# print(min_cost([1, 4, 6, 7, 8, 20], [2, 7, 15], [1, 7, 30]))


def activitySelection(arr:[[]]):
    a = arr
    ans = 1
    a.sort(key = lambda x:x[1])
    first = a[0][1]
    for i in range(1,len(arr)):
        if a[i][0]>=first:
            ans += 1
            first = a[i][0]


    return ans

def fractional_knapsack(wt:[],val:[],c:int):
    a = [[wt[i],val[i],val[i]/wt[i]] for i in range(0,len(wt))]
    a.sort(key = lambda x:x[2],reverse=True)
    print(a)
    ans = 0
    for val in a:
        if c>=val[0]:
            ans += val[1]
            c -= val[0]
        else:
            ans += c * val[2]
            c = 0
            break
    return ans

print(fractional_knapsack([7,4,6,5,6],[21,24,12,40,30],20))





# print(knap_sack([1,2,3],[10,15,40],6))



