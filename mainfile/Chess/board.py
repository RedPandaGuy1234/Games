import chess


def new_game():
    return chess.Board()


def make_move(board: chess.Board, move_uci: str) -> bool:
    try:
        move = chess.Move.from_uci(move_uci)
        if move in board.legal_moves:
            board.push(move)
            return True
        return False
    except ValueError:
        return False


def get_game_over_message(board: chess.Board) -> str:
    if board.is_checkmate():
        winner = "Black" if board.turn == chess.WHITE else "White"
        return f"Checkmate! {winner} wins."
    if board.is_stalemate():
        return "Stalemate! The game is a draw."
    if board.is_insufficient_material():
        return "Draw by insufficient material."
    if board.is_seventyfive_moves():
        return "Draw by the 75-move rule."
    if board.can_claim_threefold_repetition():
        return "Draw by threefold repetition."
    return "The game has ended in a draw."


def play_game():
    board = new_game()

    print("Welcome to Chess! Enter moves in UCI format (e.g. e2e4).")
    print("Type 'quit' at any time to exit.\n")

    while not board.is_game_over(claim_draw=True):
        print(board)
        turn_name = "White" if board.turn == chess.WHITE else "Black"
        print(f"\n{turn_name} to move.")

        move_uci = input("Enter your move: ").strip()

        if move_uci.lower() == "quit":
            print("Thanks for playing!")
            return

        if make_move(board, move_uci):
            print()
        else:
            print("That's not a legal move. Please try again (e.g. e2e4).\n")

    print(board)
    print(f"\n{get_game_over_message(board)}")


if __name__ == "__main__":
    play_game()
