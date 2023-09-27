
# global variable
total = 1000000  # the total moves
count = 0 # count the total moves

print(f'''
========= Welcome to 8-Puzzle Game! =========\n
You are given {total} moves to solve the problem!
''')

# print the puzzle in standard form
def puzzle_list(puzzle):
    n = 0
    for i in puzzle:
        n = n + 1
        print('%4s' % i, end='')
        if n % 3 == 0:  # 3 numbers a line for the 8-puzzle
            print('')
    return 

# move a number to the empty space
def move_number(number, puzzle):
    global total, count
    empty_index = puzzle.index(' ')
    number_index = puzzle.index(str(number))
    
    # Define the possible move directions as (row_change, col_change)
    move_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Check if the number can be moved to the empty space in any of the four directions
    for direction in move_directions:
        row_change, col_change = direction
        new_row = empty_index // 3 + row_change
        new_col = empty_index % 3 + col_change

        if 0 <= new_row < 3 and 0 <= new_col < 3 and puzzle[new_row * 3 + new_col] == str(number):
            # Valid move: Swap the empty space with the selected number
            puzzle[empty_index], puzzle[new_row * 3 + new_col] = puzzle[new_row * 3 + new_col], puzzle[empty_index]
            puzzle_list(puzzle)
            total -= 1
            count += 1
            return
    
    print("Invalid move! Try again.")

puzzle = ['5', '4', ' ', '6', '1', '8', '7', '3', '2']

while True:
    puzzle_list(puzzle)
    while total != 0:
       
        if puzzle == ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
            print(f'Congratulations! You solved the puzzle in {count} moves')
            break
        else:
            number = input('Enter the number you want to move: ')
            if number.isdigit() and 1 <= int(number) <= 8:
                move_number(int(number), puzzle)
            else:
                print("Invalid input! Enter a number within the range")
                continue
    break
print(f"You've consumed your {count} moves. You Failed!")
