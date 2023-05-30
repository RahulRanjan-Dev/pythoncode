def find_combinations(lst, key):
    combinations = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            #print(range(i + 1, len(lst)))
            #print(lst[j])
            if lst[i] + lst[j] == key:
                combinations.append((lst[i], lst[j]))

    return combinations if combinations else 'Not Found'


# Test the function
lst = [1, 2, 3, 4, 6, 7, 2]
key = 4
result = find_combinations(lst, key)
print(result)
