import chess

board = chess.Board()

print("\n===== CHESS BOARD =====\n")
print(board)

print("\n===== INFORMATION =====\n")

print("Uppercase Pieces = White")
print("Lowercase Pieces = Black\n")

print("White Pieces:")
print("P = Pawn")
print("R = Rook")
print("N = Knight")
print("B = Bishop")
print("Q = Queen")
print("K = King")

print("\nBlack Pieces:")
print("p = Pawn")
print("r = Rook")
print("n = Knight")
print("b = Bishop")
print("q = Queen")
print("k = King")

print("\nBoard Coordinates:")
print("Files (Columns): a b c d e f g h")
print("Ranks (Rows):    1 2 3 4 5 6 7 8")

print("\nWhite starts at ranks 1 and 2")
print("Black starts at ranks 7 and 8")

print("\nWhite moves UP the board (towards rank 8)")
print("Black moves DOWN the board (towards rank 1)")