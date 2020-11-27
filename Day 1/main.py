def get_weight_input():
    weight_int = []

    weight_input_file = open("input.txt", "r")
    if weight_input_file.mode == "r":
        weight_string = weight_input_file.read()
        weight_string_split = weight_string.split("\n")

        for weight in weight_string_split:
            weight_int.append(int(weight))
    return weight_int

def calculate_fuel(module_weight):
    total_fuel = 0
    while module_weight > 8:
        module_weight = int((module_weight / 3)) - 2
        total_fuel += module_weight
    return total_fuel

def main():
    total_fuel = 0
    weight = get_weight_input()

    for module_weight in weight:
        total_fuel += calculate_fuel(module_weight)
        print(total_fuel)
    print(total_fuel)


if __name__ == "__main__":
    main()
