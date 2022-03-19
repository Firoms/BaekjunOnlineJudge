# 체스판 다시 칠하기
import sys

N, M = map(int, sys.stdin.readline().split())
min_change = 64
chess_board = []
for i in range(N):
    chess_line = list(sys.stdin.readline().split())
    chess_board.append(chess_line)


for n in range(N - 7):
    for m in range(M - 7):
        cnt = 0
        checking = True  # True는 B, False는 W
        for i in range(8):
            checking = not checking
            for j in range(8):
                if checking and chess_board[n + i][m + j] == "W":
                    cnt += 1
                if not checking and chess_board[n + i][m + j] == "B":
                    cnt += 1
