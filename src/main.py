def Agente_JuanDaniel_Alejandro(board, player):
  return "GANE"


def initBoard():
  return [(0 for x in range(10)) for y in range (10)]

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
    Agente_JuanDaniel_Alejandro(board, 1)
    Agente_JuanDaniel_Alejandro(board, 2)
    printBoard(board)
    break



if __name__ == '__main__':
  main()