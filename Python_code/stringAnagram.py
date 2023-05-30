def stringAnagram(dictionary, query):
    anagram_counts = []

    for q in query:
        print(q)
        q_sorted = sorted(q)
        print(q_sorted)
        count = 0

        for word in dictionary:
            if sorted(word) == q_sorted:
                count += 1

        anagram_counts.append(count)

    return anagram_counts


# Test the function
dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'staris', 'raits']
query = ["a", "nark", "bs", "ba", "stari"]
result = stringAnagram(dictionary, query)
print(result)
