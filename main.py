# найти самый длинный префикс
# ["abc", "abv", "abcd"] → "ab"
# ["a", "b"] → ""


def get_longest_prefix(prefixes: list[str]) -> str:
    """Получает самый длинный префикс"""

    # print(len(min(prefixes)))

    min_range = len(min(prefixes))
    # min_range = len(min(prefixes, key=len))
    # print(min_range)

    # min_range1 = min([len(i) for i in prefixes])
    # print(min_range1)

    longest_prefix = ''
    for index in range(min_range):
        _common_prefix = prefixes[0][index]
        for prefix in prefixes:
            # if _common_prefix == prefix[index]:
            #     longest_prefix += _common_prefix

            if _common_prefix != prefix[index]:
                return longest_prefix
        else:
            longest_prefix += _common_prefix

    return longest_prefix

    # for item in range(min_range1):
    #     pass

    # longest_prefix = ''
    # for _ in prefixes:
    #     for letter in range(min_range1):
    #         if letter not in longest_prefix:
    #             longest_prefix += letter
    #

    # min(prefixes, key=lambda x: print(x))
    # print(min(prefixes))


#     longest_prefix = ''
#     for prefix in prefixes:
#         for letter in prefix:
#             if letter not in longest_prefix:
#                 longest_prefix += str(letter)
#
#


print(get_longest_prefix(["abc", "abv", "abcd", "abnaj"]))
