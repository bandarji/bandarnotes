def cascade_digits(number):
    """Display digits from a number.
    Args:
        number: str, representation of a an integer
    Returns:
        None
    """
    nums = list(number)
    digits = ''
    while nums:
        digits = nums.pop() + digits
        print(digits)

cascade_digits('498')
