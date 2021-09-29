# Python Coding Style

Next to consistency as a main aspect of good code, the second most important aspect is a certain style which the average `python` programmer is capable to read and understand properly. Therefore the following documents states the essential naming conventions.
> Here is a link for a more detailed dive into the [`PEP8 - Style Guide for Python Code'](https://www.python.org/dev/peps/pep-0008/)

## Naming conventions
### Variables

The name of a variable should be as accurate as possible and as short as possible at the same time.

*Example:*
```py
# don't
x
x = 10 + 5
# do
res
res = 10 + 5
```
A variable can be used in two different scenarios.

**Global variables** are defined outside of all functions, usually on top of the program. They should only be used if absolutely necessary. A global variable will hold their value throughout the lifetime of the program.
Global variables should be defined in a **snake_case** style, when possible at the start of the file. If the variable should only be used in it's module the name should start and end with two underscores.

*Example:*
```py
global_variable
__private_global_variable__
```

**Local variables** are defined, initially set and consumed within a function, method or block. These variables lifetime is confined within the lifetime (time of execution) of a function (method or block).
Local variables should be defined the same way as global variables.
```py
local_variable
```

### Constants
Constants are expressions with a fixed value. They are defined on a global (modul) level. The naming convention for constants prescribes that all letters are upper case letters with snake case subdivision

*Example:*
```py
PI_VALUE = 3.14159
```

### Functions
Functions should be named in **snake_case** like variables. Eventhough Python isn't strictly typesafe it ist good practice to define a return-type and the type of the parameters

*Example:*
```py
def example_function(some_value: int) -> bool:
   # do some stuff
```

### Classes (Types, Template parameters)
*Python* is a object-oriented programming language. Therefore it's all about creating objects which contain both data and functions for a certain task.

A class as well as an object should be defined with **PascalCase** notation.

**Methods and Attributes:**
The first parameter of the `__init__` function should always be called `self`. Private methods or attributes always start with two underscores.

*Example:*
```py
class Car:
    brand
    max_speed
    power
    __current_speed

    def __init__(self, ini_brand, ini_speed, ini_power){
       self.brand = ini_brand
       self.max_speed = ini_speed
       self.power = ini_power
    }
```

### Comments
If the section of code is not clearly understandable there should be a short description of the current function in form of a comment.

*Example*
```py
# divides up two double values
def division(dividend: float, divisor: float) -> float:
   return (dividend / divisor)
```

**Documentation:**

The documentation of the written code is created automatically. To provide the needed Information every function, class or method needs a docstring with a special format.

*Example:*
```py
def some_function(some_variable: int) -> int:
    """
      <Description>

      Arguments:
        some_variable: <Description>

      Returns: <Description
    """
```

**Head of File:**

In order to get quick information about the `.py` files purpose there should be a docstring at the beginning of the file.

*Example:*
```py
#!/usr/bin/env python3

"""
Created: <MM/DD/YY>
by: <Author>

<Description>
"""
```