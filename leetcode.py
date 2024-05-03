def minWindow(s, t) -> str:

    if t > s:
        return ""

    left = 0
    right = 0

    t_map = {}
    valid = {}

    for x in t:
        if x not in t_map:
            t_map[x] = 1
        else:
            t_map[x] += 1

    while left < len(s):
        letter = s[left]

        if letter in t_map:
            if t_map[letter] > 0:
                t_map[letter] -= 1


s = "ADOBECODEBANC"
t = "ABC"

minWindow(s, t)
