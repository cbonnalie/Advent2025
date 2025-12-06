def get_input(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]

    except FileNotFoundError:
        print(f'Error: File {filename} not found')
        return []


def process_input(input_text):
    sep_index = input_text.index('')

    ranges = [
        (int(line.split('-')[0]), int(line.split('-')[1]))
        for line in input_text[:sep_index]
        ]

    ids = [
        int(line)
        for line in input_text[sep_index + 1:]   
        ]

    return ranges, ids
    

def find_spoiled_ingredients(ranges, ids):
    count = 0
    
    for id in ids:
        for range in ranges:
            low = range[0]
            high = range[1]
            if id >= low and id <= high:
                count += 1
                break

    return count

    
def main():
    input_text = get_input('input.txt')
    ranges, ids = process_input(input_text)
    count = find_spoiled_ingredients(ranges, ids)
    print(count)

if __name__ == '__main__':
    main()