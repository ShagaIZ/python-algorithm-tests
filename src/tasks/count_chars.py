def count_chars(s):
    res = {}
    for char in s:
        res[char] = res.get(char, 0) + 1
    return res