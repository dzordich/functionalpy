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
