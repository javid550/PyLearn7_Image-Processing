import cv2

chess_board = cv2.imread("session 26_1\white.png")
square_size = chess_board.shape[0] // 8
board_size = 8

for row in range(board_size) :
    for col in range(board_size) :
        if (row + col) % 2 == 0 :
            top_left = (col * square_size , row * square_size)
            bottom_right = ((col + 1) * square_size, (row+1) * square_size)
            cv2.rectangle(chess_board , top_left , bottom_right , (0 , 0 , 0) , -1)

cv2.imshow("Chessboard" , chess_board)
cv2.waitKey()

cv2.imwrite("session 26_1\chess.jpg" , chess_board)