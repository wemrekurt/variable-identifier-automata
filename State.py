import re

class State:
  def __init__(self, name, inital_state = False, finish_state = False):
    self.name = name
    self.inital_state = inital_state
    self.finish_state = finish_state
    self.connections = []
  
  def connect(self, other, rule):
    self.connections.append({ 'rule': rule, 'node': other })

  def start(self, string):
    if self.inital_state:
      self.go(string, 0)
    else:
      print('This is not an initial state')

  def go(self, string, index):
    if (index < len(string)):
      found = False
      for i in self.connections:
        if re.findall(i['rule'], string[index]):
          found = True
          i['node'].go(string, index+1)
      if not found:
        print('Dump State. Error:\n' + string)
        print((" " * index) + '^')
        print('Syntax Error: " ' + string + ' " is not valid.\n')
    elif self.finish_state:
      print('Finish state. ' + string + ' is valid.\n')
