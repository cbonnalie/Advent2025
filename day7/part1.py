from re import split


def get_input(filename):
    try:
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f'Error: {filename} not found')
        return []

def find_start_position(manifold):
    for col, char in enumerate(manifold[0]):
        if char == 'S':
            return (0, col)
    return None

def simulate_beam(manifold, start_row, start_col, rows, processed_splitters):
    new_beams = []
    row = start_row

    while row < rows - 1:
        row += 1
        cell = manifold[row][start_col]

        if cell == '^':
            splitter_pos = (row, start_col)
            if splitter_pos not in processed_splitters:
                processed_splitters.add(splitter_pos)
                new_beams.append((row, start_col - 1))
                new_beams.append((row, start_col + 1))
            break

    return new_beams


def count_beam_splits(manifold):
    rows = len(manifold)
    start_pos = find_start_position(manifold)

    processed_splitters = set()
    active_beams = [start_pos]

    while active_beams:
        next_beams = []
        for beam_row, beam_col in active_beams:
            new_beams = simulate_beam(manifold, beam_row, beam_col, rows, processed_splitters)
            next_beams.extend(new_beams)

        active_beams = next_beams

    return len(processed_splitters)


def main():
    manifold = get_input('input.txt')
    split_count = count_beam_splits(manifold)
    print(split_count)


if __name__ == '__main__':
    main()