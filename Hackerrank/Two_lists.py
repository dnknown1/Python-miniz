def subset(s1, s2):
    s = list(s1)
    while s:
        if s.pop() in s2:
            return 'Yes'
    return 'No'