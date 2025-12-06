import time

def get_input(filename):
    input_rows = []
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                input_rows.append(line.strip())
            return input_rows

    except FileNotFoundError:
        print(f'Error: {filename} not found.')
        return ''

    return ''


def create_matrix(input_rows):
    row_count = len(input_rows) + 2
    col_count = len(input_rows[0]) + 2

    matrix = [ ['.' for i in range(col_count)] for j in range(row_count)]

    for r in range(1, row_count - 1):
        for c in range(1, col_count - 1):
            matrix[r][c] = input_rows[r-1][c-1]

    return matrix


def count_accessible_rolls(roll_matrix):
    row_count = len(roll_matrix) - 1
    col_count = len(roll_matrix[0]) - 1
    accessible_rolls = 0

    for r in range(1, row_count):
        for c in range(1, col_count):
            if roll_matrix[r][c] != '@':
                continue

            adjacent = 0

            if roll_matrix[r-1][c-1] == '@':
                adjacent += 1
            if roll_matrix[r-1][c] == '@':
                adjacent += 1
            if roll_matrix[r-1][c+1] == '@':
                adjacent += 1
            if roll_matrix[r][c-1] == '@':
                adjacent += 1
            if roll_matrix[r][c+1] == '@':
                adjacent += 1
            if roll_matrix[r+1][c-1] == '@':
                adjacent += 1
            if roll_matrix[r+1][c] == '@':
                adjacent += 1
            if roll_matrix[r+1][c+1] == '@':
                adjacent += 1

            if adjacent < 4:
                roll_matrix[r][c] = 'x'
                accessible_rolls += 1
                
    return accessible_rolls


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    input_rows = get_input('input.txt')
    roll_matrix = create_matrix(input_rows)

    roll_count = 0
    while(True):
        picked_up = count_accessible_rolls(roll_matrix)
        roll_count += picked_up
        if picked_up == 0:
            break

    print(roll_count)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    elapsed = (time.perf_counter() - start) * 1000
    print(f'ran in {elapsed:.03f} ms')