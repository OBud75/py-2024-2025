import re

def extract_and_sum_mul_instructions(input_data):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_data)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

with open("day3input.txt", "r") as file:
    corrupted_memory = file.read()

print(extract_and_sum_mul_instructions(corrupted_memory))

