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
            valid = True
            id_str = str(i)
            str_len = len(id_str)

            for num_len in range(1, str_len):
                if not valid:
                    break

                if str_len % num_len != 0:
                    continue

                segments = str_len // num_len
                nums = []

                start = 0
                end = num_len

                while start < str_len:
                    num = int(id_str[start:end])
                    nums.append(num)
                    start += num_len
                    end += num_len

                diff_found = False
                for j in range(1, segments):
                    if nums[0] != nums[j]:
                        diff_found = True
                        break

                if not diff_found:
                    total += i
                    valid = False

    print(total)

if __name__ == '__main__':
    main()
