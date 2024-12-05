class LocationDistanceCalculator:
    def __init__(self, left_list, right_list):
        self.left_list = left_list
        self.right_list = right_list

    def calculate_total_distance(self):
        left_sorted = sorted(self.left_list)
        right_sorted = sorted(self.right_list)

        total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

        return total_distance


def read_input_file():
    left_list = []
    right_list = []

    with open("./day1input.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


left_list, right_list = read_input_file()

calculator = LocationDistanceCalculator(left_list, right_list)

print(calculator.calculate_total_distance())
