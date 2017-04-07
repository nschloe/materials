# -*- coding: utf-8 -*-
#

# [1] https://en.wikipedia.org/wiki/Water_(molecule)#Density_of_water_and_ice
# [2] https://en.wikipedia.org/wiki/Viscosity#Water
# [3]
# https://en.wikipedia.org/wiki/Heat_capacity#Table_of_specific_heat_capacities
# [4] https://en.wikipedia.org/wiki/List_of_thermal_conductivities
# [5] Standard reference data for the thermal conductivity of water;
#     J. Phys. Chem. Ref. Data 24, 1377 (1995);
#     <http://www.nist.gov/data/PDFfiles/jpcrd493.pdf>.
# [6]
# http://www.tainstruments.co.jp/application/pdf/Thermal_Library/Applications_Notes/TN015.PDF
# [7]
# https://en.wikipedia.org/wiki/Properties_of_water#Density_of_water_and_ice


def density(T):
    # Least-squares fit from [7].
    return (
        - 1.407e-07 * (T - 273.15)**4
        + 4.387e-05 * (T - 273.15)**3
        - 0.00767 * (T - 273.15)**2
        + 0.05444 * (T - 273.15)
        + 999.9
        )


def dynamic_viscosity(T):
    # [2]
    return 2.414e-5 * 10**(247.8 / (T - 140))


def kinematic_viscosity(T):
    return dynamic_viscosity(T) / density(T)


def specific_heat_capacity(T):
    # Least-squares fit from [6].
    return (
        + 3.22e-06 * T**4
        - 0.004298 * T**3
        + 2.155 * T**2
        - 480.7 * T
        + 4.439e+04
        )


def thermal_conductivity(T):
    # [5]
    return 0.6065 * (-1.48445 + 4.12292*(T/298.15) - 1.63866*(T/298.15)**2)
