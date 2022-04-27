def even_number_of_evens(nums):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "The function requires a list. you entered {value}"
    Should raise a ValueError if the list is empty
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(nums, list) is False:
        raise TypeError(f"The function requires a list. you entered {nums}.")
    elif len(nums) < 1:
        raise ValueError("Empty list found. Enter a list with at least 1 item")
    else:
        even_nums = sum([1 for n in nums if n % 2 == 0])
        return True if even_nums != 0 and even_nums % 2 == 0 else False


if __name__ == '__main__':
    print(even_number_of_evens([2, 1, 2]))
