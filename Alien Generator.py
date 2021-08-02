



def alien_genrator(g:int):

    arr = [g]
    for k in range(1,g):
        i = 1
        ans = k+i-1
        while ans<g:
            i += 1
            ans += k+i-1
        if ans == g:
            arr.append(ans)

    return len(arr)


t= int(input())

for i in range(0,t):
    g = int(input())
    print(f"Case #{i+1}: {alien_genrator(g)}")