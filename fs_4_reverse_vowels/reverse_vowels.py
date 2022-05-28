def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiouAEIOU'

    lst = list(s)
    curr_vowels = []

    for i in range(len(lst)):
        if lst[i] in vowels:
            curr_vowels.append(lst[i])
            lst[i] = None

    curr_vowels.reverse()

    for vowel in curr_vowels:
        lst[lst.index(None)] = vowel

    return ''.join(lst)
