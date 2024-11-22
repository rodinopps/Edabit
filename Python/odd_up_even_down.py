def transform(lst):
    new = []
    for i in lst:
        if i % 2 == 0:
            new.append(i - 1)
        else:
            new.append(i + 1)
    return new
