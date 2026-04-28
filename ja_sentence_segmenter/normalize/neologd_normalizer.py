"""ãƒ†ã‚­ã‚¹ãƒˆã�®æ­£è¦�åŒ–å‡¦ç�†.

æ­£è¦�åŒ–ã�®ã‚³ãƒ¼ãƒ‰ã�¯ä»¥ä¸‹ã‚’å�‚è€ƒã�«ä¸€éƒ¨ä¿®æ­£ã‚’åŠ ã�ˆã�¦ã�„ã�¾ã�™ã€‚
https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja#python-written-by-hideaki-t--overlast
"""
from __future__ import unicode_literals

import re
import unicodedata
from typing import Dict, Generator, Iterator, List, Union, overload


def __unicode_normalize(cls: str, s: str) -> str:
    pass


def __remove_extra_spaces(s: str) -> str:
    pass


def __normalize_neologd(s: str, remove_tildes: bool) -> str:
    pass


def __normalize_iter(texts: Iterator[str], remove_tildes: bool) -> Generator[str, None, None]:
    pass


@overload
def normalize(arg: str, remove_tildes: bool = False) -> Generator[str, None, None]:
    ...


@overload
def normalize(arg: List[str], remove_tildes: bool = False) -> Generator[str, None, None]:
    ...


@overload
def normalize(arg: Iterator[str], remove_tildes: bool = False) -> Generator[str, None, None]:
    ...


def normalize(arg: Union[str, List[str], Iterator[str]], remove_tildes: bool = False) -> Generator[str, None, None]:
    """Normalize text with mecab-ipadic-neologd rules.

    Parameters
    ----------
    arg : Union[str, List[str], Iterator[str]]
        texts you want to normalize.
    remove_tildes : bool, optional
        whether to remove tildes, by default False

    Yields
    ------
    Generator[str, None, None]
        normalized texts.
    """
    pass
