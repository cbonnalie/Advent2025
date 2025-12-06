
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
    
    num_1 = 0
    num_2 = 0

    for i in range(0, bank_length):
        num = int(bank[i])

        if num > num_1 and i < bank_length - 1:
            num_1 = num
            num_2 = 0
        elif num > num_2:
            num_2 = num

    return (num_1 * 10) + num_2

def main():
    input_text = get_input('input.txt')

    sum = 0
    for line in input_text:
        joltage = get_joltage(line)
        sum += joltage

    print(sum)

if __name__ == '__main__':
    main()
