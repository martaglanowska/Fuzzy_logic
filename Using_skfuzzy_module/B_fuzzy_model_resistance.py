#scikit-fuzzy module installed

import numpy as np
import skfuzzy as fuzz  #https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

from comparison_functions import obliqueThrowAirResistance

d = ctrl.Antecedent(np.arange(0, 20, 0.1), 'd')
angle = ctrl.Antecedent(np.arange(0, 90, 0.1), 'angle')
k = ctrl.Antecedent(np.arange(0, 1, 0.01), 'k')
m = ctrl.Antecedent(np.arange(0.1, 20, 0.1), 'm')
v0 = ctrl.Consequent(np.arange(0, 30, 0.1), 'v0')

#membership functions for v0 (target)
v0['slow'] = fuzz.trimf(v0.universe, [0, 0, 5])
v0['moderate'] = fuzz.trapmf(v0.universe, [5, 12, 16, 20])
v0['fast'] = fuzz.trimf(v0.universe, [20, 30, 30])

#membership functions for d
d['small'] = fuzz.trimf(d.universe, [0, 0, 10])
d['medium'] = fuzz.trimf(d.universe, [0, 10, 20])
d['big'] = fuzz.trimf(d.universe, [10, 20, 20])

#membership functions for angle
angle['bad1'] = fuzz.trapmf(angle.universe, [0, 0, 5, 10])
angle['optimum'] = fuzz.trimf(angle.universe, [5, 45, 85])
angle['bad2'] = fuzz.trapmf(angle.universe, [80, 85, 90, 90])

#membership functions for k
k['small'] = fuzz.trimf(k.universe, [0, 0, 0.3])
k['medium'] = fuzz.trapmf(k.universe, [0.2, 0.3, 0.4, 0.5])
k['big'] = fuzz.trimf(k.universe, [0.4, 1, 1])

#membership functions for m
m['small'] = fuzz.trimf(m.universe, [0, 0, 1])
m['medium'] = fuzz.trimf(m.universe, [1, 1.5, 2])
m['big'] = fuzz.trimf(m.universe, [2, 14, 20])

#rules
rule1 = ctrl.Rule(d['small'], v0['slow'])
rule2 = ctrl.Rule(d['medium'], v0['moderate'])
rule3 = ctrl.Rule(d['big'], v0['fast'])

rule4 = ctrl.Rule(m['small'] & k['big'], v0['fast'])
rule5 = ctrl.Rule(m['medium'] & k['big'], v0['moderate'])
rule6 = ctrl.Rule(~((m['small'] & k['big']) | (m['medium'] & k['big'])), v0['slow'])

rule7 = ctrl.Rule((m['small'] & angle['optimum']) | ((m['small'] | m['medium']) & (angle['bad1'] | angle['bad2'])), v0['fast'])
rule8 = ctrl.Rule(m['medium'] & angle['optimum'], v0['moderate'])
rule9 = ctrl.Rule(m['big'], v0['slow'])

rule10 = ctrl.Rule(angle['optimum'], v0['slow'])
rule11 = ctrl.Rule(angle['bad1'] | angle['bad2'], v0['fast'])

#control system
v0_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11])

#simulation
v0_simulation = ctrl.ControlSystemSimulation(v0_ctrl)


#-----TESTS-----

#Distance
d = np.arange(1, 21, 1)
d_res = [obliqueThrowAirResistance(i, 45, 0.5, 2) for i in d]

v0_simulation.input['d'] = 10
v0_simulation.input['angle'] = 45
v0_simulation.input['k'] = 0.5
v0_simulation.input['m'] = 2
fuzz_res = []
for i in d:
  v0_simulation.input['d'] = i
  v0_simulation.compute()
  fuzz_res.append(v0_simulation.output['v0'])

f1 = plt.figure()
plt.plot(d, d_res, label = "formula")
plt.plot(d, fuzz_res, label = "fuzzy")
plt.xlabel('d')
plt.ylabel('v0')
plt.ylim(0, 30)
plt.legend()
plt.savefig("B_distance_estimation_reality")
plt.show()

#Angle
angle = np.arange(1, 89, 1)
angle_res = [obliqueThrowAirResistance(5, i, 0.5, 10) for i in angle]

v0_simulation.input['d'] = 5
v0_simulation.input['angle'] = 45
v0_simulation.input['k'] = 0.5
v0_simulation.input['m'] = 10
fuzz_res = []
for i in angle:
  v0_simulation.input['angle'] = i
  v0_simulation.compute()
  fuzz_res.append(v0_simulation.output['v0'])

f2 = plt.figure()
plt.plot(angle, angle_res, label = "formula")
plt.plot(angle, fuzz_res, label = "fuzzy")
plt.xlabel('angle')
plt.ylabel('v0')
plt.ylim(0, 30)
plt.legend()
plt.savefig("B_angle_estimation_reality")
plt.show()

#Air resistance
k = np.arange(0.1, 1, 0.01)
k_res = [obliqueThrowAirResistance(10, 45, i, 15) for i in k]

v0_simulation.input['d'] = 10
v0_simulation.input['angle'] = 45
v0_simulation.input['k'] = 0.5
v0_simulation.input['m'] = 15

fuzz_res = []
for i in k:
  v0_simulation.input['k'] = i
  v0_simulation.compute()
  fuzz_res.append(v0_simulation.output['v0'])

f3 = plt.figure()
plt.plot(k, k_res, label = "formula")
plt.plot(k, fuzz_res, label = "fuzzy")
plt.xlabel('k')
plt.ylabel('v0')
plt.ylim(0, 30)
plt.legend()
plt.savefig("B_air_resistance_estimation_reality")
plt.show()

#Weight
m = np.arange(1, 21, 1)
m_res = [obliqueThrowAirResistance(10, 20, 0.5, i) for i in m]

v0_simulation.input['d'] = 10
v0_simulation.input['angle'] = 20
v0_simulation.input['k'] = 0.5
v0_simulation.input['m'] = 10
fuzz_res = []
for i in m:
  v0_simulation.input['m'] = i
  v0_simulation.compute()
  fuzz_res.append(v0_simulation.output['v0'])

f4 = plt.figure()
plt.plot(m, m_res, label = "formula")
plt.plot(m, fuzz_res, label = "fuzzy")
plt.xlabel('m')
plt.ylabel('v0')
plt.ylim(0, 30)
plt.legend()
plt.savefig("B_weight_estimation_reality")
plt.show()