import secrets

def mixed_list(parentlist: list[list[str]]):
    mixed = []
    non_empty = [sublist for sublist in parentlist if sublist]

    while non_empty:
        sublist = secrets.choice(non_empty)
        if sublist:
            rand_index = secrets.randbelow(len(sublist))
            mixed.append(sublist.pop(rand_index))
        else:
            non_empty.remove(sublist)  # safe to skip if using `if sublist` above

    password = ''.join(mixed)
    print(f"Your password is: {password}")
