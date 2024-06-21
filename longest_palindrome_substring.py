def longest_palindrome_substring(s):
    def pal(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(s)):
        palindrome1 = pal(i, i)
        palindrome2 = pal(i, i + 1)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
input_string = "abdbsdabca"
print(longest_palindrome_substring(input_string))
