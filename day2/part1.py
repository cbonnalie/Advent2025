def read_input(filename):
    instructions = ''
    try:
        with open(filename, 'r') as f:
            for line in f:
                instructions = line.strip()

    except FileNotFoundError:
        print(f'Error: {filename} not found.')
    
    return instructions


def main():
    raw_input = read_input('input.txt')
    split_input = raw_input.split(',')

    ranges = []
    total = 0

    for num_range in split_input:
        first_id, last_id = num_range.split('-')
        ranges.append((first_id, last_id))

    for id_range in ranges:
        first_id = int(id_range[0])
        last_id = int(id_range[1])

        for i in range(first_id, last_id + 1):
            id_str = str(i)
            str_len = len(id_str)

            if str_len % 2 != 0:
                continue

            midpoint = str_len // 2
            num1, num2 = int(id_str[:midpoint]), int(id_str[midpoint:])
            
            if num1 == num2:
                total += i

    print(total)

if __name__ == '__main__':
    main()
