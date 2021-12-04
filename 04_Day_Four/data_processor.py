# gets the string that reads the numbers for the bingo game
def get_bingo_numbers(input_data):
    relevant_data = input_data[0]
    number_strings = relevant_data.split(',')
    num_numbers = len(number_strings)
    numbers = [0] * num_numbers
    for i in range(num_numbers):
        numbers[i] = int(number_strings[i])
    return numbers


# saves the bingo boards as lists of 25 integers
def get_bingo_boards(input_data):
    bingo_boards = []
    relevant_data = input_data[2:]
    while len(relevant_data) >= 5:
        new_board = []
        for i in range(5):
            next_line = []
            for j in range(5):
                next_line.append(int(relevant_data[i][3*j:3*j+2]))
            new_board.append(next_line)
        bingo_boards.append(new_board)
        relevant_data = relevant_data[6:]
    return bingo_boards


# generates an array with a specified number of empty check-boards
def gen_check_boards(i):
    check_boards = [[[0] * 5 for x in range(5)] for y in range(i)]
    return check_boards


# returns the column-representation of a bingo board or check-board
def get_bingo_columns(board):
    new_board = []
    for i in range(5):
        next_column = []
        for j in range(5):
            next_column.append(board[j][i])
        new_board.append(next_column)
    return new_board


# checks for a bingo board whether it has won or not by examining the corresponding check-board
def check_for_win(check_board):
    won = False
    for row in check_board:
        if row == [1, 1, 1, 1, 1]:
            won = True
    columns = get_bingo_columns(check_board)
    for column in columns:
        if column == [1, 1, 1, 1, 1]:
            won = True
    return won


# check whether a board has a certain bingo number and update the check-board accordingly
def play_number(number, bingo_board, check_board):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == number:
                check_board[i][j] = 1


# prints a board in a more readable format
def print_board(board):
    output = ''
    for i in range(5):
        output += str(board[i]) + "\n"
    return output


# prints a list of boards in a more readable format
def print_boards(boards):
    output = ''
    for board in boards:
        output += print_board(board) + "\n"


# gets the sum of unmarked cells from a bingo board by comparing with the check board
def compute_unmarked_sum(bingo_board, check_board):
    unmarked_sum = 0
    for i in range(5):
        for j in range(5):
            unmarked_sum += bingo_board[i][j] * (1-check_board[i][j])
    return unmarked_sum


# generates output text
def gen_output(input_data):
    output_text = ""
    bingo_numbers = get_bingo_numbers(input_data)
    num_numbers = len(bingo_numbers)
    bingo_boards = get_bingo_boards(input_data)
    num_boards = len(bingo_boards)
    check_boards = gen_check_boards(num_boards)
    game_running = True
    numbers_played = 0
    winners_found = 0
    winner = 0
    winning_number = 999
    while game_running and numbers_played < num_numbers:
        for i in range(num_boards):
            number = bingo_numbers[numbers_played]
            # print("Playing number " + str(number) + " on board nr. " + str(i))
            play_number(number, bingo_boards[i], check_boards[i])
            # print_board(bingo_boards[i])
            # print_board(check_boards[i])
        numbers_played += 1
        for i in range(num_boards):
            if check_for_win(check_boards[i]):
                winners_found += 1
                winner = i
                winning_number = number
                output_text += "After " + str(numbers_played) + " numbers played "
                output_text += "board nr. " + str(i+1) + " has won the game.\n"
                output_text += "The winning number is " + str(winning_number) + " and the board looks as follows\n\n"
                output_text += print_board(bingo_boards[i]) + "\n"
                output_text += print_board(check_boards[i])
                winning_sum = compute_unmarked_sum(bingo_boards[i], check_boards[i])
                output_text += "\n\nThe sum of all unmarked numbers is " + str(winning_sum)
                output_text += " and therefore the final score is " + str(winning_sum*winning_number) + "."
        if winners_found > 0:
            game_running = False
    return output_text
