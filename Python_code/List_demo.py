def check_sum_property(lst):
    running_sum = 0

    for i in range(len(lst)):
        running_sum += lst[i]
        print(running_sum)

        if running_sum != i + 1:
            return False

    return True

# Test cases
input1 = [1,1,1,1]
output1 = check_sum_property(input1)
print(output1)  # False




