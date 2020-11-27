def get_programm_code():
    intcode = []

    programm_code_file = open("input.txt", "r")
    if programm_code_file.mode == "r":
        programm_string = programm_code_file.read()
        programm_string_split = programm_string.split(",")

        for intcode_str in programm_string_split:
            intcode.append(int(intcode_str))
    return intcode


def handle_opcode(opcode, number_1, number_2):
    result = 0
    if opcode == 1:
        result = number_1 + number_2
    if opcode == 2:
        result = number_1 * number_2

    return result


def run_intcode(intcode):
    instruction_pointer = 0
    done = False
    output = []

    while not done:
        opcode = intcode[instruction_pointer]
        parameter_1_address = intcode[instruction_pointer + 1]
        parameter_2_address = intcode[instruction_pointer + 2]
        parameter_3_address = intcode[instruction_pointer + 3]
        if opcode == 1 or opcode == 2:
            intcode[parameter_3_address] = handle_opcode(opcode,
                                                         intcode[parameter_1_address],
                                                         intcode[parameter_2_address])
            instruction_pointer += 4
        elif opcode == 99:
            output.append(intcode[0])
            output.append(opcode)
            done = True
        else:
            output.append(0)
            output.append(opcode)
            #print("Error")
    return output


def main():
    intcode_result = []
    result = []
    #    intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

    for noun in range(100):
        for verb in range(100):
            intcode = get_programm_code()
            intcode[1] = noun
            intcode[2] = verb
            result = run_intcode(intcode)
            if result[1] == 99 and result[0] == 19690720:
                intcode_result[0] = noun
                intcode_result[1] = verb
        print("noun = %d and verb = %d", noun, verb)

    print(intcode_result)


if __name__ == '__main__':
    main()
