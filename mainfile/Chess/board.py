import chess
import chess.engine

DIFFICULTY_LEVELS = {
    "normal": 1400,
    "hard": 2000,
}
STOCKFISH_PATH = "stockfish"


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


def start_engine(path: str = STOCKFISH_PATH) -> chess.engine.SimpleEngine:
    """Launch Stockfish as a subprocess and open a UCI connection to it.

    Raises FileNotFoundError if the `stockfish` binary isn't on PATH.
    """
    return chess.engine.SimpleEngine.popen_uci(path)


def choose_bot_move(
    engine: chess.engine.SimpleEngine,
    board: chess.Board,
    elo: int,
    think_time: float = 1.0,
) -> chess.Move:

    engine.configure({"UCI_LimitStrength": True, "UCI_Elo": elo})
    result = engine.play(board, chess.engine.Limit(time=think_time))
    return result.move


def choose_difficulty() -> int:
    choice = (
        input("Choose a difficulty — Normal (~1400 elo) or Hard (~2000 elo)? (n/h): ")
        .strip()
        .lower()
    )
    return DIFFICULTY_LEVELS["hard"] if choice == "h" else DIFFICULTY_LEVELS["normal"]


def play_game():
    board = new_game()

    print("Welcome to Chess! Enter moves in UCI format (e.g. e2e4).")
    print("Type 'quit' at any time to exit.\n")

    bot_color = None
    bot_elo = None
    engine = None

    play_bot = input("Play against the bot? (y/n): ").strip().lower()
    if play_bot == "y":
        color_choice = (
            input("Should the bot play White or Black? (w/b): ").strip().lower()
        )
        bot_color = chess.WHITE if color_choice == "w" else chess.BLACK
        bot_elo = choose_difficulty()

        try:
            engine = start_engine()
        except FileNotFoundError:
            print(
                "\nCouldn't find the Stockfish engine on your PATH. See the "
                "README for install instructions for your OS. Continuing as "
                "a human vs. human game instead.\n"
            )
            bot_color = None
            bot_elo = None

    try:
        while not board.is_game_over(claim_draw=True):
            print(board)
            turn_name = "White" if board.turn == chess.WHITE else "Black"
            print(f"\n{turn_name} to move.")

            if bot_color is not None and board.turn == bot_color:
                bot_move = choose_bot_move(engine, board, bot_elo)
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
    finally:
        if engine is not None:
            engine.quit()


if __name__ == "__main__":
    play_game()
