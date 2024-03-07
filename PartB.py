from itertools import product, combinations

total_combinations = 6 * 6
sums = [0] * 11
for i in range(1, 7):
    for j in range(1, 7):
        sums[i+j-2] += 1

target_probabilities = []
for i in range(2, 13):
    target_probabilities.append(sums[i-2]/total_combinations)

def undoom_dice(Die_A, Die_B):
    flag = 0
    New_Die_A = []
    New_Die_B = []
    values = [1, 2, 3, 4]
    all_combinations = list(product(values, repeat=6))
    lists_A = [combo for combo in all_combinations if list(combo) == sorted(combo)]

    values = [1, 2, 3, 4, 5, 6, 7, 8]
    lists_B = list(combinations(values, 6))

    for i in range(0, len(lists_B)):
        for j in range(0, len(lists_A)):
            sums = [0] * 11
            for x in range(0, len(lists_B[i])):
                for y in range(0, len(lists_A[j])):
                    sums[lists_B[i][x] + lists_A[j][y] - 2] += 1  
            prob = []
            for z in range(2, 13):
                prob.append(sums[z-2]/total_combinations)
            if target_probabilities == prob:
                flag = 1
                New_Die_B = lists_B[i]
                New_Die_A = lists_A[j]
                break
        if flag == 1:
            break

    return New_Die_A, New_Die_B, prob

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B, probabilities = undoom_dice(Die_A, Die_B)

print("Original Die A:", Die_A)
print("Original Die B:", Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)