from node import Node
from expectimax import *
from ai import *

def Agente_JuanDaniel_Alejandro(board, player):
  root = Node(None, board)
  expandNode(root, player)
  return root

def initBoard(numCols, numRows):
  return [[0 for x in range(numCols)] for y in range (numRows)]


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

def exampleAI():
  board = initBoard(11,11)
  root = Node(None, board)
  expandNode(root, 1)
  root.printNode()
  root.getChild(10).printNode()

def exampleTree():
  root = Node(None, "Raiz")
  Node.addSuccesor(root, "Hijo 1")
  root.print()
  root.getChild(0).print()

if __name__ == '__main__':
  # exampleTree()
  exampleAI()
