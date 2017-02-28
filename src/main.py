import time
import numpy as np

from node import Node
from expectimax import *
from ai import *

RED = 1
BLUE = 2

def initBoard(numCols, numRows):
  return np.array([[0 for x in range(numCols)] for y in range (numRows)])

def checkWinner(board):
  # player BLUE
  for x in range(len(board[0])):
    if board[0][x] == RED:
      if(checkLine(board, RED, 0,x)):
        print("ROJO GANA")
        exit()

  # player BLUE
  for y in range(len(board)):
    if board[y][0] == BLUE:
      if(checkLine(board, BLUE, y, 0)):
        print("AZUL GANA")
        exit()

  return False


def checkLine(board, player, i, j):
  if player == RED:
    if i >= len(board)-1:
      return True

    if board[i+1][j] == RED:
      return checkLine(board, RED, i+1, j)
    if board[i+1][j+1] == RED:
      return checkLine(board, RED, i+1, j+1)

    return False

  if player == BLUE:
    if j >= len(board)-1:
      return True

    if board[i][j+1] == BLUE:
      return checkLine(board, BLUE, i, j+1)
    if board[i+1][j+1] == BLUE:
      return checkLine(board, BLUE, i+1, j+1)

    return False

def main():
  board = initBoard()
  while(True):
    move = Agente_JuanDaniel_Alejandro(board, 1)
    board[move[0]][move[1]] = 1
    move = Agente_JuanDaniel_Alejandro(board, 2)
    board[move[0]][move[1]] = 2
    printBoard(board)
    break

def exampleAI():
  board = initBoard(11,11)
  root = Node(None, board)



if __name__ == '__main__':
  exampleAI()
