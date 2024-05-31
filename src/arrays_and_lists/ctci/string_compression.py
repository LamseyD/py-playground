def string_compression(input: str) -> str:
    if not input:
        return "" 
    
    # Utilizing string builder to instead of resizing everytime, we can append to the list then finally build
    compressed = []
    count = 0
    # Iterate through the input
    for i in range(len(input)):
        # Increase count at each iteration
        count += 1
        # If we reach the end of the input or the current character is not equal to the next characterq
        if i + 1 >= len(input) or input[i] != input[i + 1]:
            compressed.append(input[i])
            compressed.append(str(count))
            # Finally reset the count
            count = 0

    return min(input, "".join(compressed), key=len)

if __name__ == '__main__':
    result = string_compression("aabcccccaaa")
    print(result)