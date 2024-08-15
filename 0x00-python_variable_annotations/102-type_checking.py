#!/usr/bin/env python3
"""type checking"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
  """return list"""
  return [i for i in lst] * factor
