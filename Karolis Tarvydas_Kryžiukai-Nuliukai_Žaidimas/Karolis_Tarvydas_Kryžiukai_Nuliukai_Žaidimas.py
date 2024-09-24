# funkcija kad parodyti kryziukų nuliukų lentelę
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Funkcija patikrinti ar yra laimėtojas
def check_winner(board, player):
    # Sąrašas visų laiminčių kombinacijų
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # eilės
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # stulpeliai
        [0, 4, 8], [2, 4, 6]              # įstrižai
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Funkcija parodyti ar lentelė pilna ir nėra laimėtojo (tai yra lygiosios)
def check_full(board):
    return ' ' not in board

# Funkcija žaidėjo judėsiui
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That spot is already taken. Choose another one.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Pagrindinė žaidimo kilpa
def tic_tac_toe():
    board = [' ' for _ in range(9)]  # Sukurti tuščią lentelę
    current_player = 'X'  # Žaidėjas X visada pirmas

    while True:
        display_board(board)  # Rodyti dabartinę lentelės būseną
        player_move(board, current_player)  # Paraginti dabartinį žaidėją atlikti ėjimą

        # Patikrina ar dabartinis žaidėjas laimėjo
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Patikrina ar rezultatas yra lygiosios
        if check_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Pakeičia žaidėjus
        current_player = 'O' if current_player == 'X' else 'X'

# Paleidžia žaidimą
if __name__ == "__main__":
    tic_tac_toe()
