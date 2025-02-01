def characterReplacement(s, k):
    left = 0
    max_freq = 0
    char_count = {}

    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_freq = max(max_freq, char_count[s[right]])

        # If too many replacements are needed, move `left` forward
        if (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example:
print(characterReplacement("AABABBA", 1))  # Output: 4
