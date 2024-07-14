class FuzzySystem:

  def __init__(self, inputVariables, outputVariable, rules):
    self.inputVariables = inputVariables
    self.outputVariable = outputVariable
    self.rules = rules
    
  def estimate(self, input):
    numerator = 0
    denominator = 0
    for r in self.rules:
      ruleActivationLevel = r.antecedent_authenticity(input)
      numerator += ruleActivationLevel * r.get_consequent()[0].get_sets()[r.get_consequent()[1]]
      denominator += ruleActivationLevel
      print("activation level: ", ruleActivationLevel, "numerator: ", numerator, "denominator: ", denominator)
    return numerator/denominator


class Input:

  def __init__(self, values):     #input like: {"food": 2, "service": 4}
    self.values = values
    
  def get_values(self):
    return self.values