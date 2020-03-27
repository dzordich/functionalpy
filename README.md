# functionalpy #

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Functionalpy provides utilities for functional programming in Python. 


### Examples ###

```python
from functionalpy import compose

add = lambda x: x + 1
square = lambda x: x * x
square_and_inc = compose(add, square)

square_and_inc(2)  # returns 5
```

```python
from functionalpy import curry

def add3(a, b, c=1):
    return a + b + c

curried_add3 = curry(add3)
curried_add3(1)  # -> (b, c=1) -> 1 + b + c
curried_add3(1)(2)  # -> 1 + 2 + 1 -> 4
curried_add3(2, c=4)(3)  # -> 2 + 3 + 4 -> 9 
```
