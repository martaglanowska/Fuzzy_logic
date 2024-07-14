class Input:

  def __init__(self, values):     #input like: {"food": 2, "service": 4}
    self.values = values
    
  def get_values(self):
    return self.values
  

class FuzzySystem:

  def __init__(self, inputVariables, outputVariable, rules):
    self.inputVariables = inputVariables
    self.outputVariable = outputVariable
    self.rules = rules

  def present_rules(self):
    for r in self.rules:
      print("Rule ", str(self.rules.index(r)+1), ":\t", r)
    
  def estimate(self, input):
    numerator = 0
    denominator = 0
    for r in self.rules:
      ruleActivationLevel = r.antecedent_authenticity(input)
      numerator += ruleActivationLevel * r.get_consequent()[0].get_sets()[r.get_consequent()[1]]
      denominator += ruleActivationLevel
      print("Rule ", str(self.rules.index(r)+1), " activation level:", ruleActivationLevel, ", numerator:", numerator, ", denominator:", denominator)
    return numerator/denominator
  
  def show_results(self, input):
    print("\n-----RESULTS-----")
    print("\nInput:\t", input.get_values(), "\n")
    for r in self.rules:
      print("Rule", str(self.rules.index(r)+1), "antecedent authenticity:", r.antecedent_authenticity(input))
    print(' ')
    print("\nValue suggested:\t", self.estimate(input), "\n")




