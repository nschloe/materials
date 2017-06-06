# -*- coding: utf-8 -*-
#
import numpy

from .helpers import mu0

# Silicon carbide.
# [1] https://en.wikipedia.org/wiki/Silicon_carbide
# [2] http://www.rgpballs.com/srv/sheet.ashx?cid=20&lng=EN
# [3] https://en.wikipedia.org/wiki/Silicon_carbide#Structure_and_properties
# [4] http://www.ioffe.rssi.ru/SVA/NSM/Semicond/SiC/thermal.html
# [6] Electrical conductivity of silicon carbide composites and fibers;
#     R. Scholz, F. dos Santos Marques, B. Riccardi;
#     <https://www.sciencedirect.com/science/article/pii/S0022311502009509>.
# [7] http://www.ceramics.nist.gov/srd/summary/scdscs.htm
# [8] Y.S. Touloukian and E.M. Buyko;
#     Specific Heat-Nonmetallic Solids;
#     Vol. 5 of Thermophysical Properties of Matter: The TPRC Data Series;
#     edited by Y.S. Touloukian and C.Y. Ho;
#     New York, 1970.
#
# [1]
melting_point = 3003.0
# [2]
magnetic_permeability = mu0
# The specific heat is temperature-dependent, see [5], [7], [8].
# Take the value for 1500 degrees Celsius here.
# TODO check out [8]
specific_heat_capacity = 1.336e3

# TODO respect temperature-dependence here
electrical_conductivity = 300.0
'''Electrical conductivity is highly temperature-dependent, see
:cite:`SSR02`. Take an approximate value for :math:`T=1000K` here.
'''


def density(T):
    '''
    [3], [4], single-crystal 3C-SiC
    A quadratic least-squares fit for the data from [4]
    (single-crystal 3C-SiC) gives

    .. math::
        \\alpha(T) = -1.05 \\times 10^{-12} T^2
                     + 3.717 \\times 10^{-9} T
                     + 2.314 \\times 10^{-6}.

    With :math:`\\rho(293)=3.21 \\times 10^3`, this gives
    '''
    return 3.2126613855078426e3 \
        * numpy.exp(1.05e-12/3.0*T**3 - 3.717e-09/2.0*T**2 - 2.314e-06*T)


def thermal_conductivity(T):
    ''':cite:`NMH97`.
    '''
    return 61.1e3 / (T - 115.0)


def thermal_diffusivity(T):
    ''':cite:`NMH97`.
    '''
    return 14.6e-3 / (T - 207.0)
