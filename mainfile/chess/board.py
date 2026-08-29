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

if __name__ == "__main__":
    board = new_game()
    print(board)
    make_move(board, "e2e4")
    print(board)
