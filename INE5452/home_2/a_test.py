def next_permutation(s):
    s = list(s)
    k = -1
    for i in range(len(s)-2, -1, -1):
        if s[i] < s[i+1]:
            k = i
            break
    if k == -1:
        return None
    l = len(s) - 1
    while l > k and s[l] <= s[k]:
        l -= 1
    s[k], s[l] = s[l], s[k]
    s[k+1:] = s[k+1:][::-1]
    return ''.join(s)


while True:
    try:
        line = input().strip()
        if line == '#':
            break
        res = next_permutation(line)
        print(res if res else "No Successor")
    except EOFError:
        break
