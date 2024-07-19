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

a) **no air resistance**

Input variables: throw distance in meters (d) and throw angle in degrees (angle)

Output variable: inicial velocity in meters per second (v0)

Rules defined:
- If d is *small* OR d is *medium* AND angle is *optimum*  **then** v0 is *slow*.
- If d is *small* AND angle is *bad* OR d is *medium* OR d is *big* AND angle is *optimum*  **then** v0 is *moderate*.
- If d is *medium* AND angle is *bad* OR d is *big* **then** v0 is fast.

Test simulation for ​​d=12 and angle=30.

<p align="center" width="100%">
<img src="https://github.com/user-attachments/assets/4e93bad3-3f5b-4ebb-a34c-2498a5c6387c" width="480" height="360">
</p>

The system responses were compared with the results from the physical formula: $`v0=\sqrt{(d/\sin(2*angle\_rad))*g}`$, where $`g=10m/s^2`$.

![image](https://github.com/user-attachments/assets/cd5b1c15-992e-4eac-9817-08299fbfa293)

Comparison of estimated and actual responses for different distances d.

<p align="center" width="100%">
<img src="https://github.com/user-attachments/assets/43902800-5a9b-45f7-a5c7-87d784bb3a2a" width="480" height="360">
</p>

b) **with air resistance**

Input variables: throw distance in meters (d), throw angle in degrees (angle), air resistance coefficient (k), body mass in kilograms (m)

Output variable: inicial velocity in meters per second (v0)

Rules defined:
- If d is *small* **then** v0 is *slow*.
- If d is *medium* **then** v0 is *moderate*.
- If d is *big* **then** v0 is *fast*.
- If k is *big* and m is *small* **then** v0 is *fast*.
- If k is *big* and m is *medium* **then** v0 is *moderate*.
- Tf there is another variation of k and m **then** v0 is *slow*.
- If m is *small* AND angle is *optimum* **then** v0 is *fast*.
- If m is *small* AND angle is *bad* OR m is *medium* AND angle is *bad* **then** v0 is *fast*.
- If m is *medium* AND angle is *optimum* **then** v0 is *moderate*.
- If m is *big* **then** v0 is *slow*.
- If angle is *optimum* **then** v0 is *slow*.
- If angle is *bad* **then** v0 is *fast*.

The system responses were compared with the results from the physical formula: $`v0=(d*k)/(m*\sin(2*angle\_rad))*\exp(-2*\sin(angle\_rad)))`$.

|                                                                                       |                                                                                       |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <img width="100%" src="https://github.com/user-attachments/assets/e94ee0ee-62b5-429b-a69e-16a1bfb39ea7"> | <img width="100%" src="https://github.com/user-attachments/assets/059a0172-f6d7-4ab1-ae69-bb382e0cb3dc"> |
| <img width="100%" src="https://github.com/user-attachments/assets/4e8f8633-1546-4a81-accb-66a42013be40"> | <img width="100%" src="https://github.com/user-attachments/assets/6f984515-29f6-4018-ba02-875023acb61c"> |

**Conclusions**

The more input variables, the more difficult it may be to create an effective fuzzy system. The above system reflects the effect of distance on velocity estimation quite well, it also tries to reflect the shape of the real graph for the throw angle, but the challenge is to define the dependencies for the k and m variables. Therefore, when creating fuzzy systems, expert knowledge is used to define the ranges of variables and rules governing a given phenomenon.

## Modules
The code was created in Python 3.11.0.
- [numpy 1.23.5](https://numpy.org/)
- [scikit-fuzzy 0.4.2](https://pythonhosted.org/scikit-fuzzy/userguide/getting_started.html)
- [matplotlib 3.6.1](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [math](https://docs.python.org/3/library/math.html)


