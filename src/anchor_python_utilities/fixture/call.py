"""Calling a module for testing with particular arguments."""

import sys
from types import ModuleType
from typing import List


def call_with_arguments(module: ModuleType, arguments: List[str]) -> None:
    """Calls a module with arguments like they were passed on the command-line.

    :param module: a module that must have a :code:`main()` function.
    :param arguments: the arguments that are passed on the command-line (ignoring any initial program-name).
    """
    sys.argv = ["arbitrary_program_name"] + arguments
    module.main()
