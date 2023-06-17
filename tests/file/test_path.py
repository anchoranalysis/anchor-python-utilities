"""Tests :mod:`file.path`"""

import os

from anchor_python_utilities import file


def test_path_same_directory() -> None:
    assert file.path_same_directory("go/a", "b.txt") == os.path.join("go", "b.txt")
