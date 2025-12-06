import time


def get_input(filename):
    input_text = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                input_text.append(line.strip())
            return input_text
    except FileNotFoundError:
        print(f'Error: {filename} not found.')
        return ''
    return ''


def get_joltage(bank):
    bank_length = len(bank)
    nums = []
    indexes = []
    
    for i in range(12):
        largest_num = 0
        index = 0
        for j in range(bank_length - 11 + i):
            num = int(bank[j])
            if num > largest_num and j not in indexes:
                if i == 0 or j > indexes[i - 1]:
                    largest_num = num
                    index = j

        nums.append(largest_num)
        indexes.append(index)
    
    joltage = 0
    for i in range(12):
        joltage += nums[11 - i] * (10 ** i)
    
    return joltage


def main():
    input_text = get_input('input.txt')
    sum = 0

    for line in input_text:
        joltage = get_joltage(line)
        sum += joltage

    print(sum)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    elapsed_time_ms = (time.perf_counter() - start) * 1000
    print(f'ran in {elapsed_time_ms:.3f} ms')
