# Bubble Sort
# Repeatedly swap adjacent elements that are out of order.
# After each pass, the largest element "bubbles" to the end.

def bubble_sort(arr):
    """
    Sorts 'arr' in-place using Bubble Sort.
    Early-exit optimization: if a full pass makes no swaps, the list is already sorted.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in the correct position
        for j in range(0, n - i - 1):
            # If the pair is out of order, swap it
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps in this pass, list is sorted → stop early
        if not swapped:
            break


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers (space-separated): ").split()))
    print("Unsorted:", nums)
    bubble_sort(nums)
    print("Sorted:  ", nums)
