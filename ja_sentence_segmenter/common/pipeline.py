"""simple pipeline generator."""
import functools
from typing import Callable, Generator


def make_pipeline(*funcs: Callable[..., Generator[str, None, None]]) -> Callable[..., Generator[str, None, None]]:
    """Make pipeline of generators.

    Parameters
    ----------
    *funcs : Callable[..., Generator[str, None, None]]
        generator you want to add pipeline.

    Returns
    -------
    Callable[..., Generator[str, None, None]]
        pipeline of generators.
    """
    pass
