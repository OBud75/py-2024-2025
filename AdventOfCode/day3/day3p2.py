import re

def extract_and_sum_with_conditions(input_data):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    mul_enabled = True
    total_sum = 0

    tokens = re.findall(f"{control_pattern}|{mul_pattern}", input_data)
    for token in tokens:
        if token[0] == "do()":
            mul_enabled = True
        elif token[0] == "don't()":
            mul_enabled = False
        
        elif token[1] and token[2]:
            if mul_enabled:
                x, y = int(token[1]), int(token[2])
                total_sum += x * y

    return total_sum

with open("day3input.txt", "r") as file:
    corrupted_memory = file.read()

print(extract_and_sum_with_conditions(corrupted_memory))

