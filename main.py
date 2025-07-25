from functools import lru_cache


@lru_cache(maxsize=None)  # Cache all results
def identify_zerolist(integers: tuple[int, ...]) -> bool:
    """Check whether the list of integers adds up to zero"""

    if not isinstance(integers, tuple):
        raise TypeError("Error: Input must be of type tuple")

    if sum(integers) == 0:
        return True
    else:
        return False


@lru_cache(maxsize=None)  # Cache all results
def find_sublist(integers: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(integers, tuple):
        raise TypeError("Error: Input must be of type tuple")

    if identify_zerolist(integers):
        return integers

    if len(integers) == 0:
        return integers
    else:
        first_list = find_sublist(integers[:-1])
        second_list = find_sublist(integers[1:])

        if len(first_list) >= len(second_list):
            return first_list
        else:
            return second_list


def main():
    """Demonstrate the zero-sum sublist algorithm with an example"""
    print("Zero-Sum Sublist Finder")
    print("=" * 30)

    # Example input
    integers = (3, 5, -8, 3, -3)
    print(f"Input: {integers}")
    print(f"Sum of input: {sum(integers)}")

    # Find the longest zero-sum sublist
    result = find_sublist(integers)
    print(f"Longest zero-sum sublist: {result}")
    print(f"Length: {len(result)}")
    print(f"Sum: {sum(result)}")

    # Additional example
    print("\n" + "=" * 30)
    integers2 = (1, 2, -3, 4, -4)
    print(f"Input: {integers2}")
    result2 = find_sublist(integers2)
    print(f"Longest zero-sum sublist: {result2}")
    print(f"Length: {len(result2)}")
    print(f"Sum: {sum(result2)}")


if __name__ == "__main__":
    main()
