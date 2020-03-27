import typing

Function = typing.Callable[..., typing.Any]

F = typing.Callable[[typing.Any, typing.Any], typing.Any]
F1 = typing.Callable[[typing.Any], typing.Callable[[typing.Any], typing.Any]]
