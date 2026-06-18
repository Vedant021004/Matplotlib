import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sharma-kohli.csv")
plt.plot(df['index'], df['V Kohli'],color = "green",marker = 'o', label = 'virat')
plt.plot(df['index'], df['RG Sharma'],color = "black",marker = 'o',label = 'Rohit')
plt.grid()
plt.legend()
plt.show()



import chess

board = chess.Board()

while not board.is_game_over():

    print("\n" + str(board))

    if board.turn:
        print("\nWhite to move")
    else:
        print("\nBlack to move")

    move = input("Move: ")

    try:
        chess_move = chess.Move.from_uci(move)

        if chess_move in board.legal_moves:
            board.push(chess_move)
        else:
            print("Illegal move")

    except:
        print("Invalid move format")

print("Game Over")