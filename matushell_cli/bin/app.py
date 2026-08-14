from argparse import ArgumentParser
from collections.abc import Callable

from matushell_cli.bin.types import Command, Flag


class App:
    __slots__ = ("_commands", "_description", "_name")

    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description
        self._commands: list[Command] = []

    def command(
        self,
        name: str,
        description: str,
        alias: str | None = None,
        flags: list[Flag] | None = None,
    ) -> Callable:
        def wrapper(func):
            self._commands.append(
                Command(
                    name=name,
                    description=description,
                    func=func,
                    alias=alias,
                    flags=(tuple(flags) if flags else ()),
                )
            )
            return func

        return wrapper

    def run(self) -> None:
        parser = ArgumentParser(prog=self._name, description=self._description)
        subparser = parser.add_subparsers(dest="command")

        for command in self._commands:
            sub = subparser.add_parser(
                command.name,
                help=command.description,
                aliases=([command.alias] if command.alias else []),
            )
            for flag in command.flags:
                args = [flag.name]
                if flag.alias:
                    args.append(flag.alias)

                sub.add_argument(*args, type=flag.type, help=flag.description)

        args = parser.parse_args()

        if args.command is None:
            parser.print_help()
            return

        kwargs = {k: v for k, v in vars(args).items() if k != "command"}

        print(args)
        print(kwargs)

        command = next(
            c
            for c in self._commands
            if c.name == args.command or c.alias == args.command
        )
        command.func(**kwargs)
