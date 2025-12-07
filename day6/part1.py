

def get_input(filename):
    input_text = []
    try:
        with open(filename, 'r') as f:
            input_text = [line.strip('\n') for line in f]
    except FileNotFoundError:
        print(f'Error: {filename} not found')
    return input_text

def get_num_lengths(input_text):
    num_lengths = []
    operands = input_text[-1]
    length = 0
    for char in operands:
        if char == '*' or char == '+':
            if length > 0:
                num_lengths.append(length)
            length = 0
        else:
            length += 1
    length += 1
    num_lengths.append(length)
    return num_lengths

def orient_equations(input_text, num_lengths):
    equations = []
    start = 0
    for length in num_lengths:
        chunk = []
        for i in range(len(input_text)):
            chunk.append(input_text[i][start:start + length])
        start += length + 1
        equations.append(chunk)
    return equations


def solve_equations(equations):
    sum = 0
    for equation in equations:
        operand = equation.pop()[0]
        result = 0
        if operand == '+':
            result = add(equation, operand)
        else:
            result = multiply(equation, operand)
        
        sum += result

    return sum

def add(equation, operand):
    nums = [int(num_string) for num_string in equation]
    sum = nums[0]

    for i in range(1, len(nums)):
        sum += nums[i]

    return sum


def multiply(equation, operand):
    nums = [int(num_string) for num_string in equation]
    product = nums[0]

    for i in range(1, len(nums)):
        product *= nums[i]

    return product


def get_results(equations):
    sum = 0
    for equation in equations:
        operand = equation[-1][0] 
        for i in range(len(equation) - 1):
            pass


def main():
    input_text = get_input('input.txt')
    num_lengths = get_num_lengths(input_text)
    equations = orient_equations(input_text, num_lengths)
    sum = solve_equations(equations)
    print(sum)


if __name__ == '__main__':
    main()