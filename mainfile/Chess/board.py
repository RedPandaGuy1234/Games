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
    info =
