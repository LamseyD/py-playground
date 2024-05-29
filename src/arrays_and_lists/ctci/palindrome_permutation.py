def palindrome_permutation(input: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # space O(n)
    seen_dict = {}
    # O(n)
    arr = list(input.replace(" ", ""))

    # O(n)
    for character in arr:
        key = character.lower()
        if character == " ":
            continue
        seen_dict[key] = seen_dict.get(key, 0) + 1

    # O(n)
    count = [""] * (len(arr) + 1)
    # O(n)
    for k, v in seen_dict.items():
        count[v] = count[v] + k

    print(count)
    # O(n)
    for i in range(1, len(arr) + 1, 2):
        print(i)
        if count[i] != "":
            if len(count[i]) > 1:
                return False
            
    return True



if __name__ == '__main__':
    result = palindrome_permutation("Tac tttcoooa")
    print(result)
