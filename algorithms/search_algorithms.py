# Binary Search (works on a sorted list)
# Idea: repeatedly cut the search range in half until the number is found (or the range is empty)

def binary_search(arr, x):
    """
    Return the index of x in arr if found, otherwise -1.
    Assumes 'arr' is sorted in non-decreasing order.
    """
    low = 0                     # start of current search range
    high = len(arr) - 1         # end of current search range

    while low <= high:          # while there is still a range to search
        mid = (low + high) // 2 # middle index of current range

        # If the middle element is the target, we are done
        if arr[mid] == x:
            return mid

        # If target is larger, ignore the left half
        if arr[mid] < x:
            low = mid + 1
        else:
            # If target is smaller, ignore the right half
            high = mid - 1

    # We end up here if x is not present
    return -1


if __name__ == "__main__":
    # Example usage: user provides a sorted list
    nums = list(map(int, input("Enter sorted numbers (space-separated): ").split()))
    target = int(input("Enter number to search: "))
    idx = binary_search(nums, target)
    print(f"Element found at index {idx}" if idx != -1 else "Not found")
