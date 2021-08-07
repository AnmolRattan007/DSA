def binary_search(arr: [], val: int, first: int, last: int):
    if first <= last:
        mid = (first + last) // 2
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            return binary_search(arr, val, mid + 1, last)
        else:
            return binary_search(arr, val, first, mid - 1)
    else:
        return -1


def peak(arr: []):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        print(mid)
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            first = mid + 1
        else:
            last = mid - 1

    return -1


def intersection(l1: [], l2: []):
    ans = set()
    s_l2 = sorted(l2)
    for i in range(0, len(l1)):
        if binary_search(s_l2, l1[i], 0, len(l2) - 1):
            ans.add(l1[i])

    return list(ans)


def binary_search_dese(arr: [], val):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = int(first + (last - first) / 2)  # To prevent integer overflow
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            last = mid - 1
        else:
            first = mid + 1

    return -1


def first_last_occurence(arr: [], val, is_first: bool):
    ans = -1
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = int(first + (last - first) / 2)
        if arr[mid] == val:
            ans = mid
            if is_first:
                last = mid - 1
            else:
                first = mid + 1
        elif arr[mid] < val:
            first = mid + 1
        else:
            last = mid - 1

    return ans


def rotated_array(arr: []):
    first = 0
    last = len(arr) - 1
    n = len(arr)
    while first <= last:
        mid = int(first + (last - first) / 2)
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return n - mid
        elif arr[mid] >= arr[first] and arr[mid] <= arr[last]:
            return first
        elif arr[mid] > arr[first]:
            first = mid + 1
        elif arr[mid] <= arr[last]:
            last = mid - 1

    return -1


# [11,12,15,18,2,5,6,8]
import sys


def elemnt_rotated_sorted_array(arr: [], val):
    pivot = rotated_array(arr)
    if arr[pivot] == val:
        return pivot
    left = binary_search(arr, val, 0, pivot - 1)
    right = binary_search(arr, val, pivot + 1, len(arr) - 1)
    if left == -1:
        return right
    else:
        return left


def floor_element(arr: [], val):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = int(first + (last - first) / 2)
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            last = mid - 1
        else:
            first = mid + 1
    return first


def ciel_element(arr: [], val):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = int(first + (last - first) / 2)
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            last = mid - 1
        else:
            first = mid + 1
        return last


def element_in_infite_array(key, arr: []):
    low = 0
    high = 1
    while key > arr[high]:
        low = high
        high *= 2

    return binary_search(arr[low:high], key, low, high)


def first_one_prob(arr: []):
    start = 0
    end = 1
    ans = -1
    while arr[end] == 0:
        start = end
        end *= 2
    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == 1:
            ans = mid
            end = mid - 1
        elif arr[mid] == 0:
            start = mid + 1

    return ans


def min_diff(arr: [], key):
    start = 0
    end = len(arr) - 1
    ans = sys.maxsize
    while start <= end:
        mid = int(start + (end - start) / 2)
        ans = min(abs(key - arr[mid]), ans)
        if arr[mid] == key:
            break
        elif key > arr[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return ans


print(min_diff([1,3,8,10,12,15], 20))
