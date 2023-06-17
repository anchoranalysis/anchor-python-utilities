"""Tests :mod:`fixture.call`"""

from anchor_python_utilities import fixture

from . import _dummy_module as dummy_module

_ARGUMENTS = ["arg_first", "arg_second"]
"""The arguments to pass to the module."""


def test_call() -> None:
    fixture.call_with_arguments(dummy_module, _ARGUMENTS)

    # Ignore the first argument when testing, as it's the name of the program on the command-line.
    assert dummy_module.last_arguments[1:] == _ARGUMENTS
