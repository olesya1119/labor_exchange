from typing import Iterable


def to_filds_list(iterable: Iterable[str]) -> str:
    return '(' + ', '.join(iterable)[:-2] + ')'


def to_values_list(values_count: int) -> str:
    return '(' + ('%s, ' * values_count)[:-2] + ')'
