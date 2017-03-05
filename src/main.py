import time
import numpy as np

from node import Node
from expectimax import *
from ai import *

ONE = 1
TWO = 2

def initBoard(numCols, numRows):
  return np.array([[0 for x in range(numCols)] for y in range (numRows)])

def makeMove(board):
  player = int(input("Ingrese jugador: "))
  y = int(input("Ingrese y: "))
  x = int(input("Ingrese x: "))
  move = [player, [y,x]]

  board[y][x] = player
  return move

def checkWinner(board):
  # player TWO
  for x in range(len(board[0])):
    if board[0][x] == ONE:
      if(checkLine(board, ONE, 0,x)):
        print("ROJO GANA")
        return True

  # player TWO
  for y in range(len(board)):
    if board[y][0] == TWO:
      if(checkLine(board, TWO, y, 0)):
        print("AZUL GANA")
        return True

  return False

def checkLine(board, player, i, j):
  if player == ONE:
    if i >= len(board)-1:
      return True

    if board[i+1][j] == ONE:
      return checkLine(board, ONE, i+1, j)
    if board[i+1][j-1] == ONE:
      return checkLine(board, ONE, i+1, j-1)
    if board[i][j-1] == ONE:
      return checkLine(board, ONE, i, j-1)
    if board[i][j+1] == ONE:
      return checkLine(board, ONE, i, j+1)

    return False

  if player == TWO:
    if j >= len(board)-1:
      return True

    if board[i][j+1] == TWO:
      return checkLine(board, TWO, i, j+1)
    if board[i-1][j+1] == TWO:
      return checkLine(board, TWO, i-1, j+1)
    if board[i+1][j] == TWO:
      return checkLine(board,TWO, i+1, j)
    if board[i-1][j] == TWO:
      return checkLine(board,TWO, i-1, j)

    return False

def main():
  board = initBoard()
  while(not checkWinner(board)):
    move = Agente_JuanDaniel_Alejandro(board, 1)
    board[move[0]][move[1]] = 1
    move = Agente_JuanDaniel_Alejandro(board, 2)
    board[move[0]][move[1]] = 2
    printBoard(board)
    break

def exampleAI():
  board = initBoard(11,11)
  root = ChangeNode(None, board, [])
  expandChangeNode(root, ONE)
  for child in root.succesors:
    expandChangeNode(child, TWO)
    for nieto in child.succesors:
      expandChangeNode(nieto, ONE)

  root.succesors[3].succesors[10].succesors[3].printNode()
  checkWinner(board)
  # print(hasVirtualConnection(root, TWO))

def exampleGame():
  board = initBoard(11,11)
  while not checkWinner(board):
    print(board)
    move = makeMove(board)
    print("Conexiones realizadas: " + str(countNewConnections(board, move)))

if __name__ == '__main__':
  exampleGame()
