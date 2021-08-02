

def binary_search(arr:[],val:int,first:int,last:int):
    if first<=last:
        mid = (first+last)//2
        if arr[mid] == val:
            return True
        elif val>arr[mid]:
            return binary_search(arr,val,mid+1,last)
        else:
           return binary_search(arr,val,first,mid-1)
    else:
        return False





def peak(arr:[]):
    first = 0
    last = len(arr)-1
    while first<=last:
        mid = (first+last)//2
        print(mid)
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
            first = mid+1
        else:
            last = mid-1

    return -1



def intersection(l1:[],l2:[]):
    ans = set()
    s_l2 = sorted(l2)
    for i in range(0,len(l1)):
        if binary_search(s_l2,l1[i],0,len(l2)-1):
            ans.add(l1[i])

    return list(ans)



