def Agente_JuanDaniel_Alejandro(board, player):
  return [0,0]


def initBoard():
  return list([[0 for x in range(10)] for y in range (10)])

def printBoard(board):
  for y in board:
    for x in y:
      print(x, end=" ")
    print(" ")

def main():
  board = initBoard()
  red = 1
  blue = 2
  while(True):
    move = Agente_JuanDaniel_Alejandro(board, 1)
    board[move[0]][move[1]] = 1
    move = Agente_JuanDaniel_Alejandro(board, 2)
    board[move[0]][move[1]] = 2
    printBoard(board)
    break



if __name__ == '__main__':
  main()