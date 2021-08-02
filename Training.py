
import sys


def training(n,p,arr,case):
    arr.sort()
    start_index = 0
    end_index = p-1

    min_hours = sys.maxsize

    while end_index<n:
        no_hours = 0
        for i in range(start_index,end_index):
            no_hours += arr[end_index] - arr[i]

        if no_hours<min_hours:
            min_hours = no_hours

        start_index += 1
        end_index += 1

    print(f"Case #{case}: {min_hours}")











if __name__ == "__main__":
    t = int(input())
    case = 1
    while t>0:
        inp = input()
        n = int(inp.split(" ")[0])
        p = int(inp.split(" ")[1])
        arr = input().split(" ")
        map_int = map(int,arr)
        int_list = list(map_int)
        training(n,p,int_list,case)
        t = t-1
        case += 1





