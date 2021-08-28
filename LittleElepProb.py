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


def solve(s, n, t):
    ans = ""
    count = 0
    for i in range(0, n):
        if i == 0:
            count += 1
            ans += str(count) + " "
            continue
        elif s[i - 1] < s[i]:
            count += 1
            ans += str(count) + " "
        else:
            count = 1
            ans += str(count) + " "
    ans.rstrip()
    print(f"Case #{t}: {ans}")


t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    solve(s, n, i + 1)
