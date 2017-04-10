# -*- coding: utf-8 -*-
#
# [1] Herington, E. F. G., Brown, I., Lane, J. E., Ambrose, D.,
#     Pure Appz.. Chem. 1976, 45, 1-9.
#     https://srdata.nist.gov/soliubility/IUPAC/SDS-29/SDS-29-pages_237.pdf
# [2] Turdukozhaeva, A.M. Russ.,
#     Temperature dependence of the dynamic viscosity of liquid mercury,
#     J. Phys. Chem. (2013) 87: 1595,
#     doi:10.1134/S0036024413090252.
#


def density(T):
    '''Least-squares fit from [1].
    '''
    return 1.542e-07 * T**2 - 0.002531 * T + 14.27


def dynamic_viscosity(T):
    '''[2].
    '''
    return 1.692e-3 * (273.0/T)**((1.00617*(373.0/T)**0.38073))


def kinematic_viscosity(T):
    return dynamic_viscosity(T) / density(T)
