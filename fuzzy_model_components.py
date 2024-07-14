class Variable:

  def __init__(self, name, min, max):
    self.name = name
    self.min = min
    self.max = max
    self.sets = dict()
  
  def __repr__(self):
    return self.name

  def triangular(self, name, a, b, c):
    if not a <= b <= c:
      return "Given values should be in ascending order"
    if c <= self.min or a >= self.max:
      return "Given values are out of Variable scope"
    self.sets[name] = ["tri", (a, b, c)]

  def trapezoidal(self, name, a, b, c, d):
    if not a <= b <= c <= d:
      return "Given values should be in ascending order"
    if d <= self.min or a >= self.max:
      return "Given values are out of Variable scope"
    self.sets[name] = ["trap", (a, b, c, d)]

  def membership_value(self, input, setName):
    if input < self.min or input > self.max:
      return "Input value too small or too big."
    if self.sets[setName][0] == 'tri':    #triangular set
      a, b, c = self.sets[setName][1]
      if input >= b:                      #considering b-c section (and using proportion)
        output =  1 - (input - b)/(c - b)
        if output < 0: return 0
        else: return output
      else:                               #considering a-b section (and using proportion) 
        output = 1 - (b - input)/(b - a)
        if output < 0: return 0
        else: return output
    else:                                 #trapezoidal set
      a, b, c, d = self.sets[setName][1]
      if input >= b:
        if input <= c:                    #considering b-c section (returning 1)
          return 1
        else:                             #considering c-d section (and using proportion)
          output = 1 - (input - c)/(d - c)
          if output < 0: return 0
          else: return output
      else:                               #considering a-b section (and using proportion)
        output = 1 - (b - input)/(b - a)
        if output < 0: return 0
        else: return output

  def get_min_max(self):
    return (self.min, self.max)
  
  def get_sets(self):
    return self.sets

 
class OutputVariable:

  def __init__(self, name):
    self.name = name
    self.sets = dict()

  def __repr__(self):
    return self.name

  def add_constant(self, name, a):
    self.sets[name] = a
  
  def get_sets(self):
    return self.sets  
  

class Rule:

  def __init__(self, antecedent, logic, consequent):
    self.antecedent = antecedent
    self.logic = logic
    self.consequent = consequent

  def __repr__(self):
    s = ""
    for i in range(len(self.logic)):
      s = s + str(self.antecedent[i]) + " " + self.logic[i] + " "
    s = s + str(self.antecedent[-1])
    return "IF " + s + " THEN " + str(self.consequent) + "."

  def antecedent_membership_levels(self, input):
    levels = []
    val = input.get_values()
    for a in self.antecedent:
      levels.append(a[0].membership_value(val[str(a[0])], a[1]))
    return levels           #input membership values for each antecedent (len(antecedents) == len(levels))

  def antecedent_authenticity(self, input):
    levels = self.antecedent_membership_levels(input)
    conjunction = self.logic.copy()
    andInd = [i for i,val in enumerate(conjunction) if val=='AND']      #ANDs before ORs - minimalization
    while andInd != []:
      ind = andInd.pop(0)
      minval = min(levels[ind], levels[ind+1])
      del conjunction[ind]
      del levels[ind:ind+2]
      levels.insert(ind, minval)
      andInd = [i for i,val in enumerate(conjunction) if val=='AND']
    return max(levels)                                                  #ORs left - maximization

  def get_consequent(self):
    return self.consequent