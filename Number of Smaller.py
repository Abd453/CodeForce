def count_smaller_elements(arr1, arr2):
    counts = []
    for num in arr2:
        count = binary_search_count(arr1, num)
        counts.append(count)
    return counts

def binary_search_count(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

# Input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Output
result = count_smaller_elements(arr1, arr2)
print(*result)
