#scikit-fuzzy module installed

import numpy as np
import skfuzzy as fuzz  #https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

from comparison_functions import obliqueThrow

d = ctrl.Antecedent(np.arange(0, 40, 0.1), 'd')
angle = ctrl.Antecedent(np.arange(0, 90, 0.1), 'angle')
v0 = ctrl.Consequent(np.arange(0, 20, 0.1), 'v0')

#membership functions for v0 (target)
v0['slow'] = fuzz.trimf(v0.universe, [0, 0, 8])
v0['moderate'] = fuzz.trimf(v0.universe, [8, 12, 16])
v0['fast'] = fuzz.trimf(v0.universe, [16, 20, 20])

#membership functions for d
d['small'] = fuzz.trimf(d.universe, [0, 0, 15])
d['medium'] = fuzz.trapmf(d.universe, [10, 15, 25, 30])
d['big'] = fuzz.trimf(d.universe, [25, 40, 40])

#membership functions for angle
angle['bad1'] = fuzz.trapmf(angle.universe, [0, 0, 30, 45])
angle['optimum'] = fuzz.trapmf(angle.universe, [30, 40, 50, 60])
angle['bad2'] = fuzz.trapmf(angle.universe, [45, 60, 90, 90])

#rules
rule1 = ctrl.Rule(d['small'] | (d['medium'] & angle['optimum']), v0['slow'])
rule2 = ctrl.Rule((d['small'] & (angle['bad1'] | angle['bad2'])) | d['medium'] | (d['big'] & angle['optimum']), v0['moderate'])
rule3 = ctrl.Rule((d['medium'] & (angle['bad1'] | angle['bad2'])) | d['big'], v0['fast'])

#control system
v0_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

#simulation
v0_simulation = ctrl.ControlSystemSimulation(v0_ctrl)
v0_simulation.input['d'] = 12       #12 meters distance
v0_simulation.input['angle'] = 30   #30 degrees angle
v0_simulation.compute()

#results
print("Estimated v0:", v0_simulation.output['v0'])   #simulation output
print("Real v0:", obliqueThrow(12, 30))              #real value

v0.view(sim=v0_simulation)  #estimated value vizualization

#estimation vs reality
fuzz_res = []
form_res = []
d = 1
while d < 31:
  v0_simulation.input['d'] = d
  v0_simulation.compute()
  fuzz_res.append(v0_simulation.output['v0'])
  form_res.append(obliqueThrow(d, 30))
  d += 1

f2 = plt.figure()
x = np.arange(1, 31, 1)
plt.plot(x, form_res, label = "formula")
plt.plot(x, fuzz_res, label = "fuzzy")
plt.xlabel('d')
plt.ylabel('v0')
plt.legend()
plt.savefig('A_estimation_reality.png')
plt.show()