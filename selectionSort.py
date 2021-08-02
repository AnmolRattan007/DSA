A = [51, 67, 32, 43, 81, 90, 75, 67, 45, 98]
for i in range(len(A)):

    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i]


def max_sub(arr: [], l):
    best = 0
    sum = 0
    for i in range(0, l):
        sum = max(arr[i], sum + arr[i])
        best = max(best, sum)

    return best


def intersection(arr1: [], arr2: []):
    a = set(arr1)
    ans = []
    for val in arr2:
        if a.__contains__(val):
            ans.append(val)
    return ans




from BinarySearch import binary_search


def intersection2(arr1: [], arr2: []):
    a = sorted(arr1)
    ans = []
    for val in arr2:
        if binary_search(a, val, 0, len(a)):
            ans.append(val)

    return ans


print(intersection2([5, 2, 8, 9, 4], [3, 2, 9, 5]))
