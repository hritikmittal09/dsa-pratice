def lengthOfLongestSubstring( s):
        l = 0  # Left pointer
        m = set()  # Set to track unique characters in the current window
        maxi = 0  # Maximum length of substring

        for r in range(len(s)):  # Right pointer
            # If the character is already in the set, remove characters until it's not
            while s[r] in m:
                m.remove(s[l])
                l += 1
            # Add the current character to the set
            m.add(s[r])
            # Update the maximum length
            maxi = max(maxi, r - l + 1)

        return maxi
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
