# -*- coding: utf-8 -*-
#
# [1] http://en.wikipedia.org/wiki/Copper
# [3] http://aries.ucsd.edu/LIB/PROPS/PANOS/cu.html
# [4] Numerical modeling of induction heating of long workpieces;
#     Chaboudez et al.;
#     IEEE Transactions on Magnetics, 30 (6), Nov. 1994;
#     <https://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=334291>.
# [5]
# https://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Values_for_some_common_materials
#
import numpy

from .helpers import mu0

# [5]
magnetic_permeability = 0.999994*mu0


def electrical_conductivity(T):
    '''The least-squares fit from :cite:`Mat79` is

    .. math::
        \\sigma(T) = \\frac{1.0}{- 0.7477\\times 10^{-8}
                                 + 0.007792\\times 10^{-8} T
                                 }.

    In better accordance with [1] (for :math:`T=293`) is the expression
    from [4],

    .. math::
        \\sigma(T) = \\frac{1.0}{-3.033\\times 10^{-9}
                                 + 68.85\\times 10^{-12} T
                                 - 6.72\\times 10^{-15} T^2
                                 + 8.56\\times 10^{-18} T^3
                                 }.
    '''
    return 1.0 / (-3.033e-9 + 68.85e-12*T - 6.72e-15*T**2 + 8.56e-18*T**3)


def density(T):
    '''[3] specifies the thermal expansion coefficient as

    .. math::
       \\alpha(T) = 10^{-6} (13.251
                             + 6.903\\times 10^{-3} T
                             + 8.5306\\times 10^{-7} T^2
                             ),

    so (with :math:`\\rho(293)=8.96\\times 10^3`) the density is derived.
    '''
    return 8.9975852012753705e3 \
        * numpy.exp(-1.0e-6 * (
                + 13.251 * T
                + 6.903e-3 / 2.0 * T**2
                + 8.5306e-7 / 3.0 * T**3
                ))


def specific_heat_capacity(T):
    # [3]
    return 316.21 + 0.3177*T - 3.4936e-4*T**2 + 1.661e-7*T**3


def thermal_conductivity(T):
    # [3]
    return 420.75 - 6.8493e-2 * T
