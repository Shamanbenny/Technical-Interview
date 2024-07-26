def find_square_pairs(L) -> list[list[int]]:
    pairs = []
    timeComplexityCounter = 0
    # O(n^2) time complexity
    for i, num_1 in enumerate(L):
        for j, num_2 in enumerate(L):
            timeComplexityCounter += 1
            if i != j and num_2 == num_1**2:
                pairs.append([num_1, num_2])

    print(f"Time Complexity: {timeComplexityCounter}")
    return pairs


print("Answers: ", find_square_pairs([16, 9, 4, 7, 8, 3, 2, 3]))
# Since n = 8, the time complexity is 8^2 = 64

print("Answers: ", find_square_pairs([15, 2, 3, 6, 5, 1, 6, 7]))
# Since n = 8, the time complexity is 8^2 = 64
