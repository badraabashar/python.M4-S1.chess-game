This code is like a chess game where you play a white piece (either a rook or a bishop) and place black pieces on a chessboard.
Then, the code checks which black pieces your white piece can "eat" (capture). Here’s how it works:

1- Create the Chessboard 🏁
The program makes an empty 8x8 chessboard with spaces for pieces.

2- Place the White Piece ⚪
The player chooses a white piece (only a rook or a bishop) and puts it on the board at a position like "a2" (a letter and a number).

3- Add Black Pieces ⚫
The player adds black pieces (pawn, rook, knight, bishop, queen, or king) to the board, up to 16 pieces.
The program ensures there aren’t too many pieces of the same type and that the pieces don’t overlap.

4- Check What the White Piece Can Capture 🎯
If the white piece is a rook, it looks in straight lines (up, down, left, right) and captures the first black piece it finds in each direction.
If the white piece is a bishop, it looks diagonally and captures the first black piece in each direction.

5- Show the Results 📢
The program prints a list of black pieces the white piece can capture.
It also displays the final chessboard with letters (a-h) and numbers (1-8).

Code Link:
https://github.com/TuringCollegeSubmissions/bbasha-PYDA.1.4/blob/main/chess.py
