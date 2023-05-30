def longest_binary_gap(N):
    # Convert N to binary
    binary = bin(N)[2:]

    # Initialize variables
    max_gap = 0
    current_gap = 0
    start_counting = False

    # Iterate over each binary digit
    for digit in binary:
        if digit == '1':
            # Start counting the gap
            start_counting = True
            # If the current gap is longer than the maximum gap, update the maximum gap
            if current_gap > max_gap:
                max_gap = current_gap
            # Reset the current gap
            current_gap = 0
        elif start_counting:
            # Increment the current gap if we are currently counting
            current_gap += 1

    return max_gap
