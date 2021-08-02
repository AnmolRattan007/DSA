


# n = int(input())
# player1 = []
# player2 = []
# for i in range(0,n):
#     val = input()
#     p1 = int(val.split(" ")[0])
#     p2  = int(val.split(" ")[1])
#     player1.append(p1)
#     player2.append(p2)
#
# d = []
# p1_score = 0
# p2_score = 0
# for i in range(0,len(player1)):
#     p1_score += player1[i]
#     p2_score += player2[i]
#     lead = p1_score-p2_score
#     if lead>0:
#         d.append([1,lead])
#     else:
#         d.append([2,abs(lead)])
#
# d.sort(key=lambda x:x[1],reverse=True)
# print(f"{d[0][0]} {d[0][1]}")
#




# def wave_arr(a:[]):
#     a.sort()
#     for i in range(1,len(a)):
#         if i%2 != 0:
#             a[i],a[i-1] = a[i-1],a[i]
#
#
#
#     return a
#
# print(wave_arr([1,2,3,4]))

#[1,2,3,4,5]

#
# def max_subarray(A:[]):
#     if len(A) == 0:
#         return 0
#     return max(A[0] + max_subarray(A[1:]), max_subarray(A[1:]))
#
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# def solve(A, B):
#     a = len(A)
#     b = len(B)
#     dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
#     for i in range(1, a + 1):
#         for j in range(1, b + 1):
#             k = dp[i - 1][j - 1] + (1 if A[i-1] == B[j-1] else 0)
#             l = dp[i - 1][j]
#             m = dp[i][j - 1]
#             dp[i][j] = max(k,l,m)
#     return dp[a][b]

# print(solve("bebdeeedaddecebbbbbabebedc","abaaddaabbedeedeacbcdcaaed"))

def stock(arr:[],n:int):
    l = len(arr)
    ans = [0]*(l+1)
    sum = 0
    for i in range(0,l):
        for j in range(i+1,l):
                if arr[i]<arr[j]:
                    ans[i] = max(ans[i],arr[j]-arr[i])
    ans.sort(reverse=True)
    print(ans)
    for k in range(0,n):
        if len(ans)>0:
            sum += ans.pop(0)

    return sum

print(stock( [ 11, 7, 11, 17, 12, 12, 16, 10, 11 ],4))


