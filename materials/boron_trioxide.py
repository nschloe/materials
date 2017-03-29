# -*- coding: utf-8 -*-
#
from .helpers import mu0

# [1] https://en.wikipedia.org/wiki/Boron_trioxide
#
# [1]
melting_point = 723.0
# [1]
boiling_point = 2133.0

# TODO include temperature dependence from [2]
density = 1.5e3
''':cite:`NMH65`.'''

# TODO include temperature dependence from :cite:`Setze57`
# 30.0 * 4.184 / 69.6182e-3 =
specific_heat_capacity = 1.802e3
''':cite:`Setze57`.'''

electrical_conductivity = 1.0 / 2.2e6
''':cite:`Setze57` (value for :math:`1000K`).'''

# # TODO fill in proper value
# thermal_conductivity = 27.0
# This is the value for boron, cf.
# <http://www.americanelements.com/bb.html>.

# TODO find out actual value
magnetic_permeability = mu0
