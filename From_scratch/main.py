from fuzzy_model_components import Variable, OutputVariable, Rule
from fuzzy_model import FuzzySystem, Input

def main():
    food = Variable("food", 0, 10)
    service = Variable("service", 0, 10)
    tip = OutputVariable("tip")

    #food.triangular("poor", -5, -1, -0.9)       #error detection: 'Given values are out of Variable scope'

    print("\n-----VARIABLE RANGES-----")
    #food - trapezoids and triangles in variable ranges
    food.trapezoidal("poor", 0, 0, 2, 4)
    food.triangular("medium", 3, 5, 7)
    food.trapezoidal("good", 6, 8, 10, 10)
    print("\nFood:   ", food.get_sets())
    #service - trapezoids and triangles in variable ranges
    service.trapezoidal("poor", 0, 0, 2, 4)
    service.triangular("medium", 3, 5, 7)
    service.trapezoidal("good", 6, 8, 10, 10)
    print("\nService:   ", service.get_sets())

    print("\n-----OUTPUT VARIABLE VALUES-----")
    #tip - constants
    tip.add_constant("small", 5)
    tip.add_constant("medium", 10)
    tip.add_constant("big", 15)
    print("\nTip:\t", tip.get_sets(), "\n")

    #rule definitions
    R1 = Rule([(food, "poor"), (service, "poor")], ['AND'], (tip, "small"))
    R2 = Rule([(food, "medium"), (service, "medium"), (food, "good"), (service, "poor"), (food, "poor"), (service, "good")], ['OR','OR','AND', 'OR', 'AND'], (tip, "medium"))
    R3 = Rule([(food, "good"), (service, "good")], ['AND'], (tip, "big"))  

    #fuzzy system initialization
    fuzzy = FuzzySystem([food, service], tip, [R1, R2, R3])
    fuzzy.present_rules()

    #values for which we want to calculate the output variable value
    inp = Input({"food": 3, "service": 8})

    #results
    fuzzy.show_results(inp)

if __name__ == '__main__':
    main()
