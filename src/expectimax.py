from random import randint
import math
# Cambiar por funcion de evaluación

def value(node):
  if len(node.succesors) == 0:
    return getUtility(node)

  if node.isMax:
    return maxValue(node)
  else:
    return expValue(node)

def maxValue(node):
  v = -math.inf

  if len(node.getSuccesors()) == 0:
    v = getUtility(node)
  else:
    for child in node.succesors:
      v = max(v, value(child))
  return v

def expValue(node):
  v = 0

  if len(node.getSuccesors()) == 0:
    v = getUtility(node)

  else:
    for child in node.succesors:
      p = 1/len(node.succesors)
      v = v + p*value(child)
  return v

def getUtility(node):
  return node.getValue()