def parenting(n, case):
    arr = []
    for j in range(0, n):
        inp = input().split(" ")
        int_lst = list(map(int, inp))
        arr.append(int_lst)
    c_arr = [arr[0]]
    j_arr = [arr[1]]
    ans = "CJ"
    for k in range(2, n):
        found = False
        for c in range(0, len(c_arr)):
            if arr[k][0] in range(c_arr[c][0]+1, c_arr[c][1]) or arr[k][1] in range(c_arr[c][0]+1, c_arr[c][1]):
                break
            else:
                if c == len(c_arr) - 1:
                    c_arr.append(arr[k])
                    ans += "C"
                    found = True
                continue

        if found == False:
            for j in range(0, len(j_arr)):
                if arr[k][0] in range(j_arr[j][0]+1, j_arr[j][1]) or arr[k][1] in range(j_arr[j][0]+1, j_arr[j][1]):
                    break
                else:
                    if j == len(j_arr) - 1:
                        j_arr.append(arr[k])
                        ans += "J"
                        found = True
                    continue
        if found == False:
            print(f"Case #{case}: IMPOSSIBLE")
            return
    print(f"Case #{case}: {ans}")


if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        parenting(n, i)
