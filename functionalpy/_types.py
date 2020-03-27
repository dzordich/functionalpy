from typing import Any, Callable


F = Callable[[Any, Any], Any]
F1 = Callable[[Any], Callable[[Any], Any]]
