# def compress_string(s):
#     compressed = ""
#     count = 1

#     for i in range(len(s)):
#         if i > 0 and s[i] == s[i - 1]:
#             count += 1
#         else:
#             if i > 0:
#                 compressed += str(count)
#             compressed += s[i]
#             count = 1
    
#     compressed += str(count)

#     return s if len(compressed) >= len(s) else compressed

# # Example usage
# input1 = "aabbcc"
# input2 = "abcd"

# print(compress_string(input1))  # Output: "a2b2c2"
# print(compress_string(input2))  # Output: "abcd"



def compress_string(s):
    """
    Compresses a string by replacing consecutive duplicate characters with the character followed by the count of consecutive duplicates.

    Args:
        s: The string to compress.

    Returns:
        The compressed string.
    """

    compressed_string = ""
    consecutive_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            consecutive_count += 1
            # print('if',s[i],consecutive_count)
        else:
            compressed_string += s[i - 1] + str(consecutive_count)
            consecutive_count = 1
            # print('else',s[i],consecutive_count)

    compressed_string += s[-1] + str(consecutive_count)
    print(len(s),s,len(compressed_string),compressed_string)
    if compressed_string == s:
        return s
    else:
        return compressed_string

    return compressed_string if len(compressed_string) < len(s) else s


print(compress_string("aabbcc"))  # Output: a2b2c2
print(compress_string("abcd"))    # Output: abcd
# print(compress_string("aa"))      # Output: a2
# print(compress_string("aaa"))     # Output: a3
