def main():
    print("Hello from google-find!")

    from functools import lru_cache

    integer_list = (3,5,-8,3)

    @lru_cache(maxsize=None)  # Cache all results
    def identify_zerolist(integers: tuple[int, ...]) -> bool:
        """Check whether the list of integers adds up to zero"""

        if not isinstance(integers, tuple):
            print("Error: Input must be of type tuple")
            return tuple()
        
        if sum(integers) == 0:
            return True
        else:
            return False

    @lru_cache(maxsize=None)  # Cache all results
    def find_sublist(integers: tuple[int, ...]) -> tuple[int, ...]:
        
        if not isinstance(integers, tuple):
            print("Error: Input must be of type tuple")
            return tuple()
        
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

    sublist = find_sublist(integer_list)

    print(sublist)


if __name__ == "__main__":
    main()
