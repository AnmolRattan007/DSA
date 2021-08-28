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


def sqrt(x):
    start = 1
    end = x
    ans = 1
    while start <= end:
        mid = int((start + end) / 2)
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1

    return ans


def sorted_2d_matrix(matrix: [[int]], target: int):
    rows = len(matrix) - 1
    col = len(matrix[0]) - 1
    i = 0

    while (i >= 0 and i <= rows) and (col >= 0 and col <= len(matrix[0]) - 1):
        j = matrix[i][col]
        if target == j:
            return True
        elif target > j:
            i = i + 1
        else:
            col = col - 1

    return False


# mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 13
# print(sorted_2d_matrix(mat, target))


def single_element_sorted(arr, first, last):
    if first >= last:
        return -1
    if single_element_helper(arr) != -1:
        return single_element_helper(arr)
    mid = int(first + (last - first) / 2)
    return max(single_element_sorted(arr[mid + 1:], last, mid + 1), single_element_sorted(arr[:mid], first, mid - 1))


def single_element_helper(arr):
    first = 0
    last = len(arr) - 1
    mid = int(first + (last - first) / 2)
    if mid > first and mid < last:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

    elif mid + 1 < len(arr) - 1:
        if arr[mid] != arr[mid + 1]:
            return arr[mid]
    elif mid - 1 >= 0:
        if arr[mid] != arr[mid - 1]:
            return arr[mid]
    return -1


# print(single_element_sorted([1, 1, 2, 3, 3, 4, 4, 8, 8], 0, 8))

def median_sorted_arrays(arr1, arr2):
    merged_arr = merge_sorted_arrays(arr1, arr2)
    first = 0
    last = len(merged_arr)
    mid = int((first + last) / 2)
    if last % 2 == 0 and mid > 0:
        return (merged_arr[mid] + merged_arr[mid - 1]) / 2
    else:
        return merged_arr[mid]


def merge_sorted_arrays(arr1, arr2):
    p1 = 0
    p2 = 0
    new = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            new.append(arr2[p2])
            p2 += 1
        else:
            new.append(arr1[p1])
            p1 += 1

    while p1 < len(arr1):
        new.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        new.append(arr2[p2])
        p2 += 1
    return new


def findMedianSortedArrays(nums1: [], nums2: []) -> float:
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    n1 = len(nums1)
    n2 = len(nums2)
    low = 0
    high = n1
    while (low <= high):
        cut1 = int((low + high) / 2)
        cut2 = int((n1 + n2 + 1) / 2) - cut1
        l1 = -sys.maxsize - 1 if cut1 <= 0 else nums1[cut1 - 1]
        l2 = -sys.maxsize - 1 if cut2 <= 0 else nums2[cut2 - 1]
        r1 = sys.maxsize if cut1 >= n1 else nums1[cut1]
        r2 = sys.maxsize if cut2 >= n2 else nums2[cut2]

        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 0:
                return float((max(l1, l2) + min(r1, r2)) / 2.0)
            else:
                return float(max(l1, l2))
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 0.0


def allocate_books(arr: [], students: int):
    low = min(arr)
    high = sum(arr)
    ans = -1
    while low <= high:
        mid = int((low + high) / 2)
        if can_allocate(mid, arr, students):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def can_allocate(limit: int, arr, s: int):
    students = 1
    sum = 0
    for val in arr:
        if val > limit:
            return False
        if sum + val > limit:
            students += 1
            sum = val
        else:
            sum = sum + val

    if students <= s:
        return True
    else:
        return False


# print(allocate_books([12, 34, 67, 90], 2))

def aggresive_cows(arr: [], cows: int):
    low = 1
    high = max(arr)-1
    while low <= high:
        mid = int((low + high) / 2)
        if placing_is_possible(cows, arr, mid):
            low = mid + 1
        else:
            high = mid - 1

    return high


def placing_is_possible(c: int, arr: [], mid):
    start = 0
    end = 1
    cows = 1
    while end < len(arr):
        if abs(arr[end] - arr[start]) >= mid:
            cows += 1
            start = end
        end += 1

    return True if cows >= c else False


