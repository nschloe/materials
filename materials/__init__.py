# -*- coding: utf-8 -*-
#
from __future__ import print_function

import pipdated

# General sources:
#
# Magnetic permeability.
# https://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Values_for_some_common_materials
# http://en.wikipedia.org/wiki/Vacuum_permeability
# http://vk1od.net/antenna/conductors/loss.htm
# https://en.wikipedia.org/wiki/Diamagnetism
#
# Electrical conductivity.
# https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity
#
# Density in kg/m^3 (liquid density for silver).
#
# Dynamic viscosity in (Pa s) (equivalent to Ns/m^2, or
# kg/(ms)).
#  *
#  http://www.engineeringtoolbox.com/air-absolute-kinematic-viscosity-d_601.html
#  * Copper: Its Trade, Manufacture, Use and Environmental Status.
#    books.google.de/books?isbn=0871706563
#
# Molar mass in g/mol.
#
# Molar heat capacity in J/(mol K).
#  * http://en.wikipedia.org/wiki/Heat_capacity
#
# Specific heat capacity in J/(kg K).
# The specific heat is calculated as
#    shc = (molar heat capacity) / (molar mass)
# With the figures from above, this pretty much coincides with the data
# from
# <http://www2.ucdsb.on.ca/tiss/stretton/database/Specific_Heat_Capacity_Table.html>.
#
# Thermal conductivity in W/(m K).
#  * http://en.wikipedia.org/wiki/List_of_thermal_conductivities
#
# Thermal diffusivity in m^2/s.
#   td = (thermal conductivity) / (density*(specific heat capacity))
#   * https://en.wikipedia.org/wiki/Thermal_diffusivity
#
#
# From the thermal expansion coefficient to the density:
#
# For the thermal expansion coefficient :math:`\\alpha`, we have
#
#     .. math::
#         \\alpha V = \\frac{dV}{dT},
#
#     so with
#
#     .. math::
#         \\frac{d\\rho}{dT}
#         = \\frac{d(m/V)}{dT}
#         = \\frac{-\\frac{dV}{dT}m}{V^2}
#         = -\\alpha \\rho
#
#     it follows
#
#     .. math::
#         \\rho(T) = C \exp(-A(T)),
#
#     where :math:`\\frac{dA}{dT}=\\alpha`.
#
from . import air
from . import argon
from . import boron_trioxide
from . import carbon_steel
from . import copper
from . import gallium_arsenide_liquid
from . import gallium_arsenide_solid
from . import graphite
from . import mercury
from . import silicon_carbide
from . import silver
from . import water


from .__about__ import (
    __version__,
    __author__,
    __author_email__
    )

if pipdated.needs_checking(__name__):
    print(pipdated.check(__name__, __version__), end='')
