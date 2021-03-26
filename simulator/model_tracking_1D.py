from typing import Callable

import numpy as np
from torch import Tensor


def derived(to_derive: Tensor, dt: Tensor) -> Tensor:
    return to_derive/dt
