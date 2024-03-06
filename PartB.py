from itertools import product

def calculate_probabilities(die):
    total_combinations = len(die) ** 2
    probabilities = [0] * 11  

    for combination in product(die, repeat=2):
        sum_value = sum(combination)
        probabilities[sum_value - 2] += 1

    probabilities = [count / total_combinations for count in probabilities]
    return probabilities

def undoom_dice(Die_A, Die_B):
    original_probabilities = calculate_probabilities(Die_A)

    def is_valid_face(face_value):
        return face_value <= 4

    New_Die_A = [0] * 6
    New_Die_B = [0] * 6

    for i in range(6):
        if is_valid_face(Die_A[i]):
            New_Die_A[i] = Die_A[i]
        else:
            New_Die_A[i] = min(Die_A[i], 4)

    for i in range(6):
        New_Die_B[i] = Die_B[i] + (Die_A[i] - New_Die_A[i])

    return New_Die_A, New_Die_B, calculate_probabilities(New_Die_A)


Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B, probabilities = undoom_dice(Die_A, Die_B)

print("Original Die A:", Die_A)
print("Original Die B:", Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
