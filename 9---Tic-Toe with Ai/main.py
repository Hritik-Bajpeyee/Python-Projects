import math

HUMAN = "O"
AI = "X"


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def Check_winner(board):

    win_lines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
    ]

    for a,b,c in win_lines:
        if board[a] == board[b] == board[c] and board[a] in [HUMAN,AI]:
            return board[a]
    return None

def board_full(board):
    return all(cell !=" " for cell in board)


def minimax(board,depth,is_max):
    winner = Check_winner(board)
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if board_full(board):
        return 0

    if is_max:
        best_score = -math.inf
        for i in range (9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(board,depth+1,False)
                board[i] = " "
                best_score = max(score,best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(board,depth+1,True)
                board[i] = " "    
                best_score = min(score,best_score)
        return best_score


def ai_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board,0,False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    
    return move

def main():
    while True:
        board = [" "] * 9
        current_player = HUMAN  # Human starts the game.
        # Inner loop: one game session.
        while True:
            print_board(board)
            # Check if the game is over.
            if Check_winner(board) or board_full(board):
                break
            if current_player == HUMAN:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if board[move] != " ":
                        print("Cell already occupied.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid move. Enter number 0-8.")
                    continue
                board[move] = HUMAN
                current_player = AI
            else:
                print("Computer's turn...")
                move = ai_move(board)
                board[move] = AI
                current_player = HUMAN

        # Game over: show final board and result.
        print_board(board)
        winner = Check_winner(board)
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a tie!")
        # Ask if the player wants to play again.
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

if __name__ =="__main__":
    main()