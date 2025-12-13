# euclidean distance
# for P(x1, y1, z1) and Q(x2, y2, z2)
# sqrt( (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2 )

import math


def get_input(filename):
    with open(filename, 'r') as f:
        return [[int(n) for n in line.strip().split(',')] for line in f]


def find_all_distances(coords):
    num_coords = len(coords)
    distances = []

    for c1 in range(num_coords):
        for c2 in range(c1 + 1, num_coords):
            dx = (coords[c1][0] - coords[c2][0]) ** 2
            dy = (coords[c1][1] - coords[c2][1]) ** 2
            dz = (coords[c1][2] - coords[c2][2]) ** 2
            distances.append([dx + dy + dz, [c1, c2]])
    
    distances.sort(reverse=True)
    return distances


def find_circuit(box, circuits):
    for i, circuit in enumerate(circuits):
        if box in circuit:
            return i
    return None


def main():
    input_file = 'input.txt'
    coords = get_input(input_file)
    circuits = [{n} for n in range(len(coords))]
    distances = find_all_distances(coords)

    while len(circuits) > 1:
        c1, c2 = distances.pop()[1]
        circ1, circ2 = find_circuit(c1, circuits), find_circuit(c2, circuits)
        if circ1 != circ2:
            circuits[circ1] = circuits[circ1] | circuits[circ2]
            del circuits[circ2]

    print(coords[c1][0] * coords[c2][0])


if __name__ == '__main__':
    main()