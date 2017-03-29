# -*- coding: utf-8 -*-
#
from .helpers import mu0

# [1] https://en.wikipedia.org/wiki/Carbon_steel
# [2]
# https://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Values_for_some_common_materials
# [3] https://en.wikipedia.org/wiki/List_of_thermal_conductivities
# [4]
# https://en.wikipedia.org/wiki/Heat_capacity#Table_of_specific_heat_capacities
#
# [1]
magnetic_permeability = 100*mu0
density = 7.85e3
# [3]
thermal_conductivity = 50.0
# stainless steel @293K:
electrical_conductivity = 1.180e6
# [4]
specific_heat_capacity = 0.466e3
