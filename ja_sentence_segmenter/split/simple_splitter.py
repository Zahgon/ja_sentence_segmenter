"""Simple sentence splitter for japanese text."""

import re
from typing import Generator, Iterator, List, Match, Union, overload

BETWEEN_QUOTE_JA_REGEX = r"ã€Œ[^ã€Œã€�]*ã€�"
BETWEEN_PARENS_JA_REGEX = r"\([^()]*\)"
ESCAPE_CHAR = "âˆ¯"
DEFAULT_PUNCTUATION_REGEX = r"ã€‚!?"
"""default punctuation characters for splitting."""


def __split_newline_iter(texts: Iterator[str]) -> Generator[str, None, None]:
    pass


@overload
def split_newline(arg: str) -> Generator[str, None, None]:
    ...


@overload
def split_newline(arg: List[str]) -> Generator[str, None, None]:
    ...


@overload
def split_newline(arg: Iterator[str]) -> Generator[str, None, None]:
    ...


def split_newline(arg: Union[str, List[str], Iterator[str]]) -> Generator[str, None, None]:
    """Split text with line boundaries.

    Parameters
    ----------
    arg : Union[str, List[str], Iterator[str]]
        texts you want to split.

    Yields
    ------
    Generator[str, None, None]
        texts splitted with line boundaries.
    """
    pass


def __split_punctuation_iter(texts: Iterator[str], punctuations: str, split_between_quote: bool, split_between_parens: bool) -> Generator[str, None, None]:
    pass


@overload
def split_punctuation(
    arg: str, punctuations: str = DEFAULT_PUNCTUATION_REGEX, split_between_quote: bool = False, split_between_parens: bool = False
) -> Generator[str, None, None]:
    ...


@overload
def split_punctuation(
    arg: List[str], punctuations: str = DEFAULT_PUNCTUATION_REGEX, split_between_quote: bool = False, split_between_parens: bool = False
) -> Generator[str, None, None]:
    ...


@overload
def split_punctuation(
    arg: Iterator[str], punctuations: str = DEFAULT_PUNCTUATION_REGEX, split_between_quote: bool = False, split_between_parens: bool = False
) -> Generator[str, None, None]:
    ...


def split_punctuation(
    arg: Union[str, List[str], Iterator[str]],
    punctuations: str = DEFAULT_PUNCTUATION_REGEX,
    split_between_quote: bool = False,
    split_between_parens: bool = False,
) -> Generator[str, None, None]:
    """Split text with puctuations.

    Parameters
    ----------
    arg : Union[str, List[str], Iterator[str]]
        texts you want to split
    punctuations : str, optional
        regular expression for puctuations, by default DEFAULT_PUNCTUATION_REGEX
    split_between_quote : bool, optional
        split if punctuation between quotes, by default False
    split_between_parens : bool, optional
        split if punctuation between parentheses, by default False

    Yields
    ------
    Generator[str, None, None]
        texts splitted with puctuations.
    """
    pass
