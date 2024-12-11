def interpolation_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
     
        if arr[high] == arr[low]:  
            if arr[low] == target:
                return low
            else:
                return -1

        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1  
        else:
            high = pos - 1  

    return -1 


# Example usage
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
target = int(input("Enter the number to search: "))

index = interpolation_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
