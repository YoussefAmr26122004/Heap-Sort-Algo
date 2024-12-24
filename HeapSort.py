def heapify(arr, n, i):
    """
    Heapify a sub-tree rooted at index i.

    Args:
        arr: The input array.
        n: Size of the heap.
        i: Index of the root of the sub-tree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the root.
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Build a max-heap from the given array.
    """
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    Sort the given array using heap sort.
    """
    n = len(arr)

    # Build a maxheap
    build_max_heap(arr)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)
