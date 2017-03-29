# -*- coding: utf-8 -*-
#
from __future__ import print_function

from . import air
from . import argon
from . import boron_trioxide
from . import carbon_steel
from . import copper
from . import gallium_arsenide_liquid
from . import gallium_arsenide_solid
from . import graphite
from . import silicon_carbide
from . import silver
from . import water


from .__about__ import (
    __version__,
    __author__,
    __author_email__
    )

import pipdated
if pipdated.needs_checking(__name__):
    print(pipdated.check(__name__, __version__), end='')
