# # import json
# #
# # json_string = '''
# # [
# # {
# # "id" : "001",
# # "x" : "7",
# # "name" : "AR"
# # },
# # {
# # "id" : "007",
# # "x" : "5",
# # "name" : "BR"
# # }
# # ]
# # '''
# #
# # json_data = json.loads(json_string)
# # print(json_data)
# #
# # for data in json_data:
# #     print(data["id"])
# #     print(data["name"])
# #
# #
#
#
# r = 1
# def case1(N, K):
#     total_time = K + N
#     global r
#     print(f"Case #{r}: {total_time}")
#     r = r + 1
#
#
# def case2(N, K, S):
#         i = N - S
#         o = K - S
#         total_time = K + i + o
#         global r
#         print(f"Case #{r}: {total_time}")
#         r = r + 1
#
#
#
#
#
#
# if __name__ == "__main__":
#     number_of_cases = int(input())
#
#     while number_of_cases > 0:
#         case = input().split(" ")
#         N = int(case[0])
#         K = int(case[1])
#         S = int(case[2])
#         if K / 2 >= S:
#             number_of_cases = number_of_cases - 1
#             case1(N, K)
#
#         elif K / 2 < S:
#             number_of_cases = number_of_cases - 1
#             case2(N, K, S)
#
#
#

count = 0
def spl(L):
    global count
    i = list(str(L)) #converting number into lsit with digits
    LL = int(len(i))
    index = 0
    while index<LL:
        chk = int(i[index])
        if index %2!=0: #if index is odd but number should be even
            if chk%2 == 0:
                if index==LL-1:
                    count=count+1
                    break
                else:
                    index = index + 1
                    continue
            else:
                break
        elif index %2==0: #if index is even but number should be odd
            if chk%2 != 0:
                if index==LL-1:
                    count=count+1
                    break
                else:
                    index = index + 1
                    continue
            else:
                break









if __name__ == "__main__":
    number_of_cases = int(input())
    r = 1
    while number_of_cases>0:
        case = input().split(" ")
        L = int(case[0])
        R = int(case[1])
        while L<=R:
            spl(L)
            L = L+1
        number_of_cases = number_of_cases-1
        print(f"Case #{r}: {count}")
        count = 0
        r+=1
        continue


# l = list(str(12345))
# print(l)