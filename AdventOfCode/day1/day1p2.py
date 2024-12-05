from collections import Counter

class LocationSimilarityCalculator:
    def __init__(self, left_list, right_list):
        self.left_list = left_list
        self.right_list = right_list

    def calculate_similarity_score(self):
        # Count occurrences of each number in the right list
        right_count = Counter(self.right_list)

        # Calculate the similarity score
        similarity_score = sum(left * right_count[left] for left in self.left_list)

        return similarity_score


def read_input_file():
    l_list = []
    r_list = []

    with open("./day1input.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            l_list.append(left)
            r_list.append(right)

    return l_list, r_list


# Read the input file
left_list, right_list = read_input_file()

# Create a calculator for the similarity score
similarity_calculator = LocationSimilarityCalculator(left_list, right_list)

# Calculate and print the similarity score
print(similarity_calculator.calculate_similarity_score())
