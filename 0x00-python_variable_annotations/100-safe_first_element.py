#!/usr/bin/env python3
"""function"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
  """return first element of list"""
  if lst:
    return lst[0]
  else:
    return None
