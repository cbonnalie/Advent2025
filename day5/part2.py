def get_input(filename):
    input_text = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line == '':
                    break 
                input_text.append(stripped_line)  
            return input_text

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []


def process_input(input_text):
    ranges = sorted(
        [list(map(int, line.strip().split('-'))) for line in input_text], key=lambda x: x[0],    
    )

    return ranges
    

def find_spoiled_ingredient_ids(id_ranges):
    merged_ranges = [(id_ranges[0])]

    for current_start, current_end in id_ranges[1:]: 
        last_merged_start, last_merged_end = merged_ranges[-1] 

        if current_start <= last_merged_end + 1:
            merged_ranges[-1][1] = max(last_merged_end, current_end)
        else:
            merged_ranges.append([current_start, current_end]) 

    total_count = 0
    for start, end in merged_ranges:
        total_count += (end - start + 1)

    return total_count


def main():
    input_text = get_input('input.txt')
    ranges = process_input(input_text)
    count = find_spoiled_ingredient_ids(ranges)
    print(count)

if __name__ == '__main__':
    main()