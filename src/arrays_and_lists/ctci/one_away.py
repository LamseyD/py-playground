def one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)

    return False

def one_edit_replace(s1: str, s2: str) -> bool:
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_insert(s1: str, s2: str) -> bool:
    index1 = 0
    index2 = 0
    # s1 is the shorter string
    # Iterate through both of the strings at the same time
    while index1 < len(s1) and index2 < len(s2):
        # If we find the difference
        if s1[index1] != s2[index2]:
            # First time we find the difference, the index should be the same
            if index1 == index2:
                # We simply move the index of the longer string forward by one
                index2 += 1
            else:
                # If we find the difference again, we return False
                return False
        else:
            # If the characters are the same, simply increase the index
            index1 += 1
            index2 += 1
    # Return true
    return True

if __name__ == '__main__':
    result = one_away("pale", "ple")
    print(result)
    result = one_away("pales", "pale")
    print(result)
    result = one_away("pale", "bale")
    print(result)
    result = one_away("pale", "bake")
    print(result)