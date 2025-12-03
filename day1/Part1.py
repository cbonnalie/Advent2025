# # Advent of Code 2025 - Day 1 Part 1

def read_input():
    rotations = []
    try:
        with open('input.txt', 'r') as f:
            for line in f:
                direction = line[0]
                amount = int(line[1:])
                tup = (direction, amount)
                rotations.append(tup)
    except FileNotFoundError:
        print("Error: file not found.")
    return rotations

def main():
   rotations = read_input()
   position = 50
   count = 0

   for rot in rotations:
       direction = rot[0]
       amount = rot[1]
       
       position = (position - amount) % 100 if (direction == "L") else (position + amount) % 100

       if position == 0:
           count += 1

   print(count)

if __name__ == "__main__":
    main()
