# -*- coding: utf-8 -*-
#
# References
# [1] http://en.wikipedia.org/wiki/Density_of_air
# [2]
# https://en.wikipedia.org/wiki/Heat_capacity#Table_of_specific_heat_capacities
# [3] http://www.engineeringtoolbox.com/air-properties-d_156.html
# [4]
# http://profmaster.blogspot.ide/2009/01/thermal-conductivity-of-air-vs.html
# [5] http://www.ohio.edu/mechanical/thermo/property_tables/air/air_Cp_Cv.html
# [6]
# https://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Values_for_some_common_materials
#
from .helpers import mu0

# [6]
magnetic_permeability = 1.00000037 * mu0
electrical_conductivity = 0.0


def density(T):
    # [1]
    return 1.2922 * 273.15/T


def specific_heat_capacity(T):
    # least-squares fit from [5]
    return 2.196e-13 * T**4 \
        - 8.916e-10 * T**3 \
        + 1.234e-06 * T**2 \
        - 0.0004807 * T \
        + 1.06


def thermal_conductivity(T):
    # [4]
    return 1.5207e-11 * T**3 \
        - 4.8574e-8 * T**2 \
        + 1.0184e-4 * T \
        - 0.00039333
