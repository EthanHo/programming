def all_unique(x):
    characters = {}
    for y in x:
        if y in characters.keys():
            return False
        else:
            characters[y]=1
    return True


def all_unique2(x):
    return True


print all_unique("Ethan")

