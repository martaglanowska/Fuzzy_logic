# Fuzzy logic

Fuzzy logic allows for intermediate values ​​between 0 and 1, unlike classical logic, which classifies values ​​as absolute true or false. In fuzzy logic, a value is expressed by belonging, usually to several sets, to a certain degree. Fuzzy systems are based on this approach and are therefore closer to the natural representation of everyday situations.

Main components of the fuzzy system are:
1. linguistic variables - input and output variables, which values ​​are expressed in words,
2. membership functions - with a domain ​​\[0,1\], defined for each linguistic term of a given variable,
3. rules - each consisting of a preceding part (IF) and a subsequent part (THEN), defining the natural relationships that occur between variables.

## Implementations

This repository contains two approaches to implementing a fuzzy system:
 * **implementation from scratch** revealing the mechanisms operating inside the system (*From_scratch* directory)
 * **using a dedicated [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html) library**, which conveniently allows the user to define and run such a system (*Using_skfuzzy_module* directory)

### Implementation from scratch
Presented on a standard example of estimating the tip amount based on the evaluation of food and service in a restaurant.

In *main.py* we define input variables (food, service), the allowable range of their values and output variable (tip). Then we define trapezoids and triangles for each input variable - note, that values ​​must be within the previously defined ranges. We define a constant for each linguistic value of the output variable.

![image](https://github.com/user-attachments/assets/fdf68e15-d9b4-495d-8096-b4a699e7b8c2)

The next step is to define the relationships between variables using rules. In this case we specify:
- antecedents list of any length
- logical operators list shorter by one element than antecedents list: AND(minimum)/OR(maximum)
- consequent

The calculation of the rule activation level will be performed in accordance with the usual order of logical operations.

![image](https://github.com/user-attachments/assets/6c093372-c7c3-43ef-8af3-b986cf09590a)

Then we initialize the fuzzy system, provide the values ​​of the input variables and get the suggested tip amount after running the file. The inference process is based on **fuzzification** (determining the degree to which the given values ​​belong to individual sets) and on the application of the **system rules**.

![image](https://github.com/user-attachments/assets/6e3901b5-6ceb-472c-853b-4957431a387a)

### Using a dedicated library
Presented on the example of estimating the initial velocity of a oblique throw without and with air resistance.

A) no air resistance

Input variables: throw distance in meters (d) and throw angle in degrees (angle)
Output variable: inicial velocity in meters per second (v0)

Rules defined:
- If d is *small* OR d is *medium* AND angle is *optimum*  **then** v0 is *slow*.
- If d is *small* AND angle is *bad* OR d is *medium* OR d is *big* AND angle is *optimum*  **then** v0 is *moderate*.
- If d is *medium* AND angle is *bad* OR d is *big* **then** v0 is fast.

The system responses were compared with the results from the physical formula: $`v0=\sqrt{d/\sin{2*angle}*g}`$, where $`g=10m/s^2`$.

Test simulation for ​​d=12 and angle=30.
![A_estimated_value](https://github.com/user-attachments/assets/09669cc6-9216-42f2-8361-86f84dc1c95f)
![image](https://github.com/user-attachments/assets/a8a40033-baf9-441f-ad20-3476c86a3c3d)

Comparison of estimated and actual responses for different distances d.
![A_estimation_reality](https://github.com/user-attachments/assets/43902800-5a9b-45f7-a5c7-87d784bb3a2a)

## Modules
The code was created in Python 3.11.0.
- [numpy 1.23.5](https://numpy.org/)
- [scikit-fuzzy 0.4.2](https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html)
- [matplotlib 3.6.1](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [math](https://docs.python.org/3/library/math.html)




