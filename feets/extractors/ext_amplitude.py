#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)

# Copyright (c) 2017 Juan Cabral

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# =============================================================================
# FUTURE
# =============================================================================

from __future__ import unicode_literals


# =============================================================================
# DOC
# =============================================================================

__doc__ = """"""


# =============================================================================
# IMPORTS
# =============================================================================

import math

import numpy as np

from .core import Extractor


# =============================================================================
# EXTRACTOR CLASS
# =============================================================================

class Amplitude(Extractor):
    """
    **Amplitude**

    The amplitude is defined as the half of the difference between the median
    of the maximum 5% and the median of the minimum 5% magnitudes. For a
    sequence of numbers from 0 to 1000 the amplitude should be equal to 475.5.


    References
    ----------

    .. [richards2011machine] Richards, J. W., Starr, D. L., Butler, N. R.,
       Bloom, J. S., Brewer, J. M., Crellin-Quick, A., ... &
       Rischard, M. (2011). On machine-learned classification of variable stars
       with sparse and noisy time-series data.
       The Astrophysical Journal, 733(1), 10. Doi:10.1088/0004-637X/733/1/10.

    """

    data = ['magnitude']
    features = ['Amplitude']

    def fit(self, magnitude):
        N = len(magnitude)
        sorted_mag = np.sort(magnitude)

        amplitude = (np.median(sorted_mag[-int(math.ceil(0.05 * N)):]) -
                     np.median(sorted_mag[0:int(math.ceil(0.05 * N))])) / 2.0
        return {"Amplitude": amplitude}
