def string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return is_substring(s1 + s1, s2)

def is_substring(s1: str, s2: str) -> bool:
    return s2 in s1

if __name__ == '__main__':
    result = string_rotation("waterbottle", "erbottlewat")
    print(result)
