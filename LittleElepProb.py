# def solve(arr:[],c:int):
#     for val in arr:
#         if c>0:
#             c = c-val
#         else:
#             print("No")
#             return
#     if c>=0:
#         print("Yes")
#     else:
#         print("No")
#
#
#
#
# t = int(input())
# for i in range(0,t):
#     inp = input()
#     n = int(inp.split(" ")[0])
#     c = int(inp.split(" ")[1])
#     a = input().split(" ")
#     arr = list(map(int,a))
#     solve(arr,c)
#
#
#
#
#
#
#


def solve(a: [], b: [], n: int):
    ans = []

    for i in range(0, n):
        p = (a[i] * 20) - (b[i] * 10)
        if p > 0:
            ans.append(p)
        else:
            ans.append(0)

    ans.sort(reverse=True)
    print(ans[0])


t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split(" ")
    a_arr = list(map(int, a))
    b = input().split(" ")
    b_arr = list(map(int, b))
    solve(a_arr, b_arr, n)
