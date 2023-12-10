def consonant_value(word):
    vowels = "aeiou"
    consonant_substrings = [substring for substring in word.split(vowels) if substring]
    values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in consonant_substrings]
    return max(values)

# Test cases
print(consonant_value("zodiacs"))  # Output: 26
print(consonant_value("strength"))  # Output: 57
