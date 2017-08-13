def all_unique(x):
    characters = {}
    for y in x:
        if y in characters.keys():
            return False
        else:
            characters[y]=1
    return True


def all_unique2(x):
    for i in range(len(x)-1):
        for j in range(i+1, len(s)):
            if x[i]==x[j]:
                return False
    return True


def permutation(x, y):
    return sorted(x)==sorted(y)


def replace_spaces(s, n):
    read_index = len(s) - (2 * n) - 1
    write_index = len(s)-1
    while read_index >= 0:
        if s[read_index] != ' ':
            s[write_index] = s[read_index]
            write_index -= 1
            read_index -= 1
        else:
            s[write_index] = '0'
            s[write_index-1] = '2'
            s[write_index-2] = '%'
            write_index -= 3
            read_index -= 1
    return s

print replace_spaces(list('aa zz  '), 1)
