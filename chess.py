def main():
    # Create an 8x8 board filled with empty spaces.
    board = [[" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "]]
    
    # Get and place the white piece (only "rook" or "bishop" allowed).
    white_piece, white_pos = get_white_piece_input(board)
    board[white_pos[1]][white_pos[0]] = ("W", white_piece)
    
    # Define allowed black pieces with their maximum counts.
    allowed_black = {"pawn": 8, "rook": 2, "knight": 2, "bishop": 2, "queen": 1, "king": 1}
    current_black_counts = {piece: 0 for piece in allowed_black}
    black_pieces = []  # To track added black pieces.
    
    # Input black pieces until the user types "done" (min 1, max 16 pieces).
    while len(black_pieces) < 16:
        print("Allowed black pieces:", list(allowed_black.keys()))
        user_input = input("Enter a black piece (e.g. 'bishop d4') or type 'done': ").strip()
        if user_input.lower() == "done":
            if not black_pieces:
                print("Error: You must add at least one black piece.")
                continue
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid format. Please enter a piece and a coordinate separated by a space.")
            continue

        piece, coord = parts[0].lower(), parts[1]
        if piece not in allowed_black:
            print(f"Invalid piece. Allowed black pieces: {list(allowed_black.keys())}")
            continue
        if current_black_counts[piece] >= allowed_black[piece]:
            print(f"Error: Maximum number of {piece}s reached ({allowed_black[piece]} allowed).")
            continue
        if not is_valid_coordinate(coord):
            print("Invalid coordinate. Use a letter (a-h) followed by a digit (1-8).")
            continue

        pos = coordinate_to_index(coord)
        if board[pos[1]][pos[0]] != " ":
            print("That square is already occupied!")
            continue

        # Place the black piece.
        board[pos[1]][pos[0]] = ("B", piece)
        black_pieces.append((piece, pos))
        current_black_counts[piece] += 1

    # Determine capturable black pieces based on the white piece type.
    if white_piece.lower() == "rook":
        capturable = get_rook_captures(board, white_pos)
    elif white_piece.lower() == "bishop":
        capturable = get_bishop_captures(board, white_pos)
    else:
        capturable = []
        print("Unexpected white piece type encountered.")

    # Print the results and the final board.
    print("\nResult:")
    if capturable:
        print("The white piece can capture the following black pieces:")
        for piece, pos in capturable:
            print(f"{piece} at {index_to_coordinate(pos)}")
    else:
        print("The white piece cannot capture any black pieces.")
    
    print("\nFinal Board:")
    print_board(board)


def is_valid_coordinate(coord):
    """Checks if a coordinate is valid (e.g. 'a1' to 'h8')."""
    return len(coord) == 2 and coord[0].lower() in "abcdefgh" and coord[1] in "12345678"


def coordinate_to_index(coord):
    """Converts a coordinate (e.g. 'a1') into 0-indexed (x, y) tuple."""
    return (ord(coord[0].lower()) - ord('a'), int(coord[1]) - 1)


def index_to_coordinate(pos):
    """Converts a 0-indexed (x, y) position back to a coordinate (e.g. 'a1')."""
    return chr(pos[0] + ord('a')) + str(pos[1] + 1)


def get_white_piece_input(board):
    """Prompts the user to input the white piece and its coordinate."""
    allowed = ["rook", "bishop"]
    while True:
        user_input = input("Enter the white piece (rook or bishop) and its coordinate (e.g. 'rook a2'): ").strip().split()
        if len(user_input) != 2:
            print("Invalid input. Format: piece coordinate.")
            continue
        piece, coord = user_input[0].lower(), user_input[1]
        if piece not in allowed:
            print("Invalid piece. Choose 'rook' or 'bishop'.")
            continue
        if not is_valid_coordinate(coord):
            print("Invalid coordinate. Use a letter (a-h) and a digit (1-8).")
            continue
        pos = coordinate_to_index(coord)
        if board[pos[1]][pos[0]] != " ":
            print("That square is already occupied!")
            continue
        print(f"White piece {piece} placed at {coord}.")
        return piece, pos


def get_rook_captures(board, white_pos):
    """
    For a white rook, scan in the four cardinal directions.
    The first encountered piece in each direction is capturable if it is black.
    """
    captures = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        x, y = white_pos
        while True:
            x += dx
            y += dy
            if not (0 <= x < 8 and 0 <= y < 8):
                break
            if board[y][x] == " ":
                continue
            if board[y][x][0] == "B":
                captures.append((board[y][x][1], (x, y)))
            break
    return captures


def get_bishop_captures(board, white_pos):
    """
    For a white bishop, scan along the four diagonal directions.
    The first encountered piece in each diagonal is capturable if it is black.
    """
    captures = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        x, y = white_pos
        while True:
            x += dx
            y += dy
            if not (0 <= x < 8 and 0 <= y < 8):
                break
            if board[y][x] == " ":
                continue
            if board[y][x][0] == "B":
                captures.append((board[y][x][1], (x, y)))
            break
    return captures


def print_board(board):
    """Prints the board with file labels (a-h) and rank numbers (1-8)."""
    print("   a b c d e f g h")
    for rank in range(0, 8, 1):
        row = []
        for cell in board[rank]:
            if cell == " ":
                row.append(".")
            else:
                color, piece = cell
                row.append(piece[0].upper() if color == "W" else piece[0].lower())
        print(f"{rank+1}  " + " ".join(row))


main()
