def get_input(filename):
    try:
        with open(filename, 'r') as f:
            manifold = [
                list(line.strip())
                for line in f
                if line.strip()
            ]

    except FileNotFoundError:
        print(f'Error: {filename} not found')

    return manifold



def initialize(manifold):
    rows = len(manifold)
    first_row = manifold[0]
    cols = len(first_row) 
    start = 0

    for c in range(len(first_row)):
        if first_row[c] == 'S':
            start = (0, c)
            break

    splitters = []

    for r in range(1, rows):
        for c in range(cols):
            if manifold[r][c] == '^':
                splitters.append((r, c))

    return rows, cols, [start], splitters



def process_splits(manifold, starts, rows):
    new_splitters = []
    new_starts = []
    for line in starts:
        curr_row, curr_col = line
        while(curr_row < rows - 1):
            curr_row += 1
            if manifold[curr_row][curr_col] == '.':
                continue
            if (curr_row, curr_col) not in new_splitters:
                new_splitters.append((curr_row, curr_col))
                if (curr_row, curr_col - 1) not in new_starts:
                    new_starts.append((curr_row, curr_col - 1))
                if (curr_row, curr_col + 1) not in new_starts:
                    new_starts.append((curr_row, curr_col + 1))
                break

    return new_starts, new_splitters


def main():
    manifold = get_input('input.txt')

    rows, cols, starts, all_splitters = initialize(manifold)
    print(f'rows: {rows}\ncols: {cols}\nstart: {starts}\n{all_splitters}')

    found_splitters = set()

    while(len(starts) > 0):
        starts, new_splitters = process_splits(manifold, starts, rows)
        for new_splitter in new_splitters:
            found_splitters.add(new_splitter)

    print(found_splitters)
    print(len(found_splitters))


if __name__ == '__main__':
    main()