def find_unique_substrings(s, k):
    unique_substrings = set()

    for i in range(len(s)):
        print(s[k])
        substring = s[i:i+k]
        if len(set(substring)) == k:
            unique_substrings.add(substring)

    return sorted(unique_substrings)


# Test the function
s = 'AABCAAFDA'
k = 3
result = find_unique_substrings(s, k)
for substring in result:
    print(substring)
