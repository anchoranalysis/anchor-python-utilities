"""Constructing paths to entities."""
import os


def path_same_directory(path_file: str, filename: str) -> str:
    """A path to a file existing in the same directory as the executing script.

    It is often convenient to call with :const:`__file__` as the first
    parameter, in order to locate a file on the file-system.

    Args:
        path_file: a path to the file that exists in some directory.
        filename: the filename to assign in the outputted path.

    Returns:
        a path to a file with the directory of :code:`path_file` with `filename` appended.
    """
    return os.path.join(os.path.dirname(path_file), filename)
