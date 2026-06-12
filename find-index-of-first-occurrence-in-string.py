def strstr(haystack, needle):
    """
        Example 1:

        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: "sad" occurs at index 0 and 6.
        The first occurrence is at index 0, so we return 0.
        Example 2:

        Input: haystack = "leetcode", needle = "leeto"
        Output: -1
        Explanation: "leeto" did not occur in "leetcode", so we return -1.

    """
    returnval = -1
    len_haystack = len(haystack)
    len_needle = len(needle)
    max_start = len_haystack - len_needle

    for ss in range(max_start + 1):
        ee = ss + len_needle - 1
        check_first = haystack[ss]
        check_last = haystack[ee]

        if check_first == needle[0] and check_last == needle[-1]:
            found_all = True
            # technically this re-checks first and last, and it doesn't have to...
            check_range = range(ee - ss + 1)
            for xx in check_range:
                ss_xx = ss + xx
                if haystack[ss_xx] != needle[xx]:
                    found_all = False
                    break
            if found_all:
                returnval = ss
                break

    return returnval


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    result = strstr(haystack, needle)
    print(result)