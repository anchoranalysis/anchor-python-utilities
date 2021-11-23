"""Tests :mod:`file.path`"""

from anchor_python_utilities import file
import os


def test_path_same_directory() -> None:
    assert file.path_same_directory("go/a", "b.txt") == os.path.join("go", "b.txt")
