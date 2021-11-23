"""A dummy module used for testing, and determining if the main function was called."""
import sys
from typing import Optional, List


last_arguments: Optional[List[str]] = None
"""Used to track whether main has been called or not."""


def main() -> None:
    global last_arguments
    last_arguments = sys.argv
