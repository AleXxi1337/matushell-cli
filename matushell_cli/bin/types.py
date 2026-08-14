from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Flag:
    name: str
    description: str
    type: type
    alias: str | None = None


@dataclass(frozen=True)
class Command:
    name: str
    description: str
    func: Callable
    alias: str | None = None
    flags: tuple[Flag, ...] = ()
