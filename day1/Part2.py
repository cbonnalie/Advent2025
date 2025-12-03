# Advent of Code 2025 - Day 1 Part 2

def solve(instructions):
    position = 50
    password = 0

    for direction, displacement in instructions:
        if direction == "R":
            password += (position + displacement) // 100

        else:
            password += ((100 - position) % 100 + displacement) // 100
            displacement *= -1

        position = (position + displacement) % 100
    print(password)

def read_input(filename):
    instructions = []
    try:
        with open(filename, "r") as f:
            for line in f:
                instructions.append(line.strip())

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    
    return instructions


def main():
   instructions = read_input("input.txt")
   solve(instructions)


if __name__ == "__main__":
    main()