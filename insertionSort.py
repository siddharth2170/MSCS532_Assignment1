def insertion_sort_desc(arr):
    """
    Sorts an array in monotonically decreasing order
    using the Insertion Sort algorithm.
    """

    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements smaller than key
        # one position ahead
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def main():
    #input array
    numbers = [12, 5, 8, 19, 1, 15]

    print("Original Array:")
    print(numbers)

    sorted_numbers = insertion_sort_desc(numbers)

    print("\nSorted Array in Monotonically Decreasing Order:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()