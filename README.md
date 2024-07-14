# Fuzzy logic

Fuzzy logic allows for intermediate values ​​between 0 and 1, unlike classical logic, which classifies values ​​as absolute true or false. In fuzzy logic, a value is expressed by belonging, usually to several sets, to a certain degree. Fuzzy systems are based on this approach and are therefore closer to the natural representation of everyday situations.

Main components of fuzzy system are:
1. linguistic variables - input and output variables, which values ​​are expressed in words,
2. membership functions - with a domain ​​\[0,1\], defined for each linguistic term of a given variable,
3. rules - each consisting of a preceding part (IF) and a subsequent part (THEN), defining the natural relationships that occur between variables.

## Implementations

This repository contains two approaches to implementing a fuzzy system:
 * **use of a dedicated [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html) library**, which conveniently allows the user to define and run such a system (*Using_skfuzzy_module* directory) - presented on the example of estimating the initial velocity of a oblique throw without and with air resistance
 * **implementation from scratch**, which undoubtedly gives more freedom in creating a fuzzy system (*From_scratch* directory) - presented on a standard example of estimating the tip amount based on the evaluation of food and service in a restaurant

## Modules
The code was created in Python 3.11.0.
- [numpy 1.23.5](https://numpy.org/)
- [scikit-fuzzy 0.4.2](https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html)
- [matplotlib 3.6.1](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [math](https://docs.python.org/3/library/math.html)




