def merge_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

# Input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Merge arrays
merged_array = merge_arrays(arr1, arr2)

# Output
print(*merged_array)
