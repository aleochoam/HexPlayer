class ChangeNode(object):
  """docstring for ChangeNode"""
  def __init__(self, parent, state, changset):
    self.succesors = []
    self.parent = parent
    self.state = states
    self.changset = changset

    def addSuccesor(self, state, changset):
      node = ChangeNode(parent, state, changset)
      parent.succesors.append(node)