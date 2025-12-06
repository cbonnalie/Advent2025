def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print(f'Error: {filename} not found.')
        return ''

    return ''


def parse_ranges(raw_input):
    ranges = []
    split_ranges = raw_input.split(',')

    for num_range_str in split_ranges:
        first_id_str, last_id_str = num_range_str.split('-')
        first_id = int(first_id_str)
        last_id = int(last_id_str)
        ranges.append((first_id, last_id))
    
    return ranges

def is_balanced(num):
    id_str = str(num)
    str_len = len(id_str)

    if str_len % 2 != 0:
        return False

    midpoint = str_len // 2

    num1_str = id_str[:midpoint]
    num2_str = id_str[midpoint:]

    return num1_str == num2_str

def find_balanced_sum(ranges):
    total = 0

    for first_id, last_id in ranges:
        for i in range(first_id, last_id + 1):
            if is_balanced(i):
                total += i

    return total

def main():
    raw_input = read_input('input.txt')
    ranges = parse_ranges(raw_input)
    total = find_balanced_sum(ranges)
    print(total)

if __name__ == '__main__':
    main()
