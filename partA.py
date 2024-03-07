from fractions import Fraction

total_combinations = 6 * 6
print("Total Combinations: ", total_combinations)

distribution = [[0 for i in range(6)] for j in range(6)]
for i in range(1, 7):
    for j in range(1, 7):
        distribution[i-1][j-1] = (i, j)

print("Distribution of Combinations:")
for row in distribution:
    print(row)

sums = [0] * 11
for i in range(1, 7):
    for j in range(1, 7):
        sums[i+j-2] += 1

print("Probability of Sums:")
for i in range(2, 13):
    probability = Fraction(sums[i-2], total_combinations)
    print(f"P(Sum = {i}) = {probability} = {round(sums[i-2]/total_combinations, 4)}")