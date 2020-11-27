from copy import deepcopy


def get_wire_input():
    programm_code_file = open("input.txt", "r")
    if programm_code_file.mode == "r":
        wire1 = programm_code_file.readline()
        wire2 = programm_code_file.readline()

        wire1_split = wire1.split(",")
        wire2_split = wire2.split(",")

        return wire1_split, wire2_split


def calculate_coordinates(wire_data):
    line_segment = {}
    segments = []
    current_coordinate = [0, 0]

    line_segment['start'] = current_coordinate[:]
    line_segment['end'] = current_coordinate[:]

    for line in wire_data:
        direction = line[0]
        line_segment['distance'] = int(line[1:])
        if direction == 'U':
            line_segment['end'][1] = line_segment['start'][1] + line_segment['distance']
            line_segment['direction'] = 'y'
            line_segment['constant'] = line_segment['start'][0]
            # current_coordinate[1] += distance
        elif direction == 'R':
            line_segment['end'][0] = line_segment['start'][0] + line_segment['distance']
            line_segment['direction'] = 'x'
            line_segment['constant'] = line_segment['start'][1]
            # current_coordinate[0] += distance
        elif direction == 'D':
            line_segment['end'][1] = line_segment['start'][1] - line_segment['distance']
            line_segment['direction'] = 'y'
            line_segment['constant'] = line_segment['start'][0]
            # current_coordinate[1] -= distance
        elif direction == 'L':
            line_segment['end'][0] = line_segment['start'][0] - line_segment['distance']
            line_segment['direction'] = 'x'
            line_segment['constant'] = line_segment['start'][1]
            # current_coordinate[0] -= distance

        line_segment['high'], line_segment['low'] = get_high_low(line_segment['start'], line_segment['end'])

        segments.append(deepcopy(line_segment))
        line_segment['start'] = line_segment['end'][:]
    return segments


def get_high_low(coordinate_1, coordinate_2):
    if coordinate_1[0] == coordinate_2[0]:
        if coordinate_1[1] > coordinate_2[1]:
            high = coordinate_1[1]
            low = coordinate_2[1]
        else:
            high = coordinate_2[1]
            low = coordinate_1[1]
    else:
        if coordinate_1[0] > coordinate_2[0]:
            high = coordinate_1[0]
            low = coordinate_2[0]
        else:
            high = coordinate_2[0]
            low = coordinate_1[0]

    return high, low


def determine_intersections(wire_1, wire_2):
    intersections = []
    intersection_steps = []
    steps_w1 = 0


    for segment_w1 in wire_1:

        steps_w2 = 0

        for segment_w2 in wire_2:

            # check if directions are opposite
            if segment_w1['direction'] != segment_w2['direction']:
                # check if it crosses
                if(segment_w2['low'] < segment_w1['constant'] < segment_w2['high'] and
                   segment_w1['low'] < segment_w2['constant'] < segment_w1['high']):

                    # Calculate manhattan distance from 0,0
                    intersections.append((abs(segment_w1['constant'])+abs(segment_w2['constant'])))

                    # Calculate steps to intersection
                    # First total of previous sections
                    total_steps = steps_w1 + steps_w2

                    # Remainder of current sections
                    if segment_w1['direction'] == 'x':
                        total_steps += abs(segment_w2['constant'] - segment_w1['start'][0])
                        total_steps += abs(segment_w1['constant'] - segment_w2['start'][1])
                    else:
                        total_steps += abs(segment_w2['constant'] - segment_w1['start'][1])
                        total_steps += abs(segment_w1['constant'] - segment_w2['start'][0])

                    intersection_steps.append(total_steps)

            steps_w2 += segment_w2['distance']
        steps_w1 += segment_w1['distance']

    return intersections, intersection_steps


def main():
    raw_wires = get_wire_input()
    wire_1, wire_2 = raw_wires

    segments_1 = calculate_coordinates(wire_1)
    segments_2 = calculate_coordinates(wire_2)

    intersections, steps = determine_intersections(segments_1, segments_2)

    print(intersections)
    print(min(steps))


if __name__ == '__main__':
    main()
