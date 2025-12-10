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
            return col
    return None


def find_hit_splitters(manifold, start_col):
    beam_index = [0] * len(manifold)
    beam_index[start_col] = 1
    
    rows = len(manifold)
    cols = len(manifold[0])

    split_count = 0

    for r in range(1, rows):
        for c in range(cols):
            if manifold[r][c] == '^' and beam_index[c] == 1:
                split_count += 1
                beam_index[c-1] = 1
                beam_index[c] = 0
                beam_index[c+1] = 1

    return split_count


def main():
    manifold = get_input('input.txt')
    start_col = find_start_position(manifold)
    split_count = find_hit_splitters(manifold, start_col)    
    print(split_count)


if __name__ == '__main__':
    main()