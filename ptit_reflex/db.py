from functools import reduce
import operator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.util import typing as sa_typing


def _make_union_type(*types):
    return reduce(operator.or_, types)


sa_typing.make_union_type = _make_union_type  # type: ignore[attr-defined]


class Base(DeclarativeBase):
    pass
