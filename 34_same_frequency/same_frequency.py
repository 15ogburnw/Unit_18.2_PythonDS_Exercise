def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    list1 = list(str(num1))
    list2 = list(str(num2))

    dict1 = {num: list1.count(num) for num in set(list1)}
    dict2 = {num: list2.count(num) for num in set(list2)}

    if dict1 == dict2:
        return True
    else:
        return False
