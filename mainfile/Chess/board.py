import random

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


def choose_bot_color() -> bool:
    choice = (
        input("Should the bot play White, Black, or Random? (w/b/r): ")
        .strip()
        .lower()
    )
    if choice == "w":
        return chess.WHITE
    if choice == "b":
        return chess.BLACK
    return random.choice([chess.WHITE, chess.BLACK])


def bot_wants_draw(
    engine: chess.engine.SimpleEngine,
    board: chess.Board,
    bot_color: bool,
    think_time: float = 1.0,
) -> bool:
    info = engine.analyse(board, chess.engine.Limit(time=think_time))
    score = info["score"].pov(bot_color).score(mate_score=100000)
    if score is None:
        return False
    return score <= 50


def play_game():
    board = new_game()

    print("Welcome to Chess! Enter moves in UCI format (e.g. e2e4).")
    print("Type 'quit' to exit, 'resign' to resign, or 'draw' to offer a draw.\n")

    bot_color = None
    bot_elo = None
    engine = None

    play_bot = input("Play against the bot? (y/n): ").strip().lower()
    if play_bot == "y":
        bot_color = choose_bot_color()
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

            if move_uci.lower() == "resign":
                winner = "Black" if board.turn == chess.WHITE else "White"
                print(f"\n{turn_name} resigns. {winner} wins!")
                return

            if move_uci.lower() == "draw":
                if bot_color is not None:
                    opponent_color = not board.turn
                    if bot_wants_draw(engine, board, opponent_color):
                        print("\nThe bot accepts your draw offer. The game is a draw.")
                        return
                    print("The bot declines your draw offer.\n")
                    continue
                accept = (
                    input("Does the other player accept the draw? (y/n): ")
                    .strip()
                    .lower()
                )
                if accept == "y":
                    print("\nDraw agreed. The game is a draw.")
                    return
                print("Draw declined.\n")
                continue

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
