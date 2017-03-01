class ChangeNode(object):
  """docstring for ChangeNode"""
  def __init__(self, parent, state, changeset):
    self.succesors = []
    self.parent = parent
    self.state = state
    self.changeset = changeset

  def addSuccesor(self, state, changeset):
    node = ChangeNode(self, state, changeset)
    self.succesors.append(node)

  def printNode(self):
    print(self.state)

  def getParent(self):
    return self.parent

  def getChild(self, index):
    if self._isIndexValid(index):
      return self.succesors[index]

  def _isIndexValid(self, index):
    if 0 <= index < len(self.succesors):
      return True
    else:
      return False