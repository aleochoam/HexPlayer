from random import random
import math

def value(node):
  if len(node.succesors) == 0:
    return getUtility(node)

  if node.isMax:
    return maxValue(node)
  else:
    return minValue(node)

def maxValue(node):
  v = -math.inf

  if len(node.getSuccesors()) == 0:
    v = getUtility(node)
  else:
    for child in node.succesors:
      v = max(v, value(child))
  return v

def minValue(node):
  v = +math.inf

  if len(node.getSuccesors()) == 0:
    v = getUtility(node)

  else:
    for child in node.succesors:
      v = min(v, value(child))
  return v

def getUtility(node):
  return node.getValue()