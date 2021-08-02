import sys


def rabbit_house(r,c,case):
    arr = [[]]
    for i in range(0,r):
        inp = input().split(" ")
        map_int = map(int, inp)
        int_list = list(map_int)
        arr.append(int_list)

    ans = 0

    for row in arr:
        max = row[0]
        max_index = 0
        for i in range(0,c):
            if row[i]>max:
                max = row[i]
                max_index = i
        for j in range(max_index,c):
            diff = abs(max-(row[j]+1))
            row[j] = diff
            ans += diff

        for k in range(max_index,-1):
            diff = abs(max-(row[k]+1))
            row[k] = diff
            ans += diff


    










if __name__ == "__main__":
    t = int(input())
    for i in range(1,t+1):
        inp = input()
        r = int(inp.split(" ")[0])
        c = int(inp.split(" ")[1])
        rabbit_house(r,c,i)