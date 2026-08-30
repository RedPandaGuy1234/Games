import chess

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0,
}


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


def evaluate_board(board: chess.Board) -> int:
    """Score the board by material. Positive favors White, negative favors Black."""
    if board.is_checkmate():
        # Whoever's turn it is has just been checkmated, so that's very bad for them.
        return -9999 if board.turn == chess.WHITE else 9999

    score = 0
    for piece_type, value in PIECE_VALUES.items():
        score += value * len(board.pieces(piece_type, chess.WHITE))
        score -= value * len(board.pieces(piece_type, chess.BLACK))
    return score


def minimax(board: chess.Board, depth: int, alpha: float, beta: float, maximizing: bool) -> float:
    """Look `depth` moves ahead, assuming both sides play their best move.

    `maximizing` is True when it's White's turn to move (White wants a high
    score) and False when it's Black's turn (Black wants a low score).
    Alpha-beta pruning skips branches that can't change the final choice.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing:
        best_score = float("-inf")
        for move in legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Black would never let this branch happen — stop looking
        return best_score
    else:
        best_score = float("inf")
        for move in legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # White would never let this branch happen — stop looking
        return best_score


def choose_bot_move(board: chess.Board, depth: int = 3) -> chess.Move:
    """Pick the best move for whoever's turn it currently is."""
    maximizing = board.turn == chess.WHITE
    best_move = None
    best_score = float("-inf") if maximizing else float("inf")

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, float("-inf"), float("inf"), not maximizing)
        board.pop()

        if maximizing and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing and score < best_score:
            best_score = score
            best_move = move

    return best_move


def play_game():
    board = new_game()

    print("Welcome to Chess! Enter moves in UCI format (e.g. e2e4).")
    print("Type 'quit' at any time to exit.\n")

    bot_color = None
    play_bot = input("Play against the bot? (y/n): ").strip().lower()
    if play_bot == "y":
        color_choice = input("Should the bot play White or Black? (w/b): ").strip().lower()
        bot_color = chess.WHITE if color_choice == "w" else chess.BLACK

    while not board.is_game_over(claim_draw=True):
        print(board)
        turn_name = "White" if board.turn == chess.WHITE else "Black"
        print(f"\n{turn_name} to move.")

        if bot_color is not None and board.turn == bot_color:
            bot_move = choose_bot_move(board)
            print(f"Bot plays: {bot_move.uci()}\n")
            board.push(bot_move)
            continue

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
