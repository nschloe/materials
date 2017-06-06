# -*- coding: utf-8 -*-
#
import numpy

from .helpers import mu0

# [1] https://en.wikipedia.org/wiki/Graphite
# [2] https://en.wikipedia.org/wiki/Carbon
# [3]
# The electric and magnetic properties of graphite;
# R.R. Haering;
# 1957;
# http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=111169&local_base=GEN01-MCG02
# [4]
# http://www.ndt-ed.org/GeneralResources/MaterialProperties/ET/ET_matlprop_Misc_Matls.htm
# [5]
# http://chemistry.stackexchange.com/questions/820/electrical-conductivity-of-graphite
# [6] Thermal and Electrical Conductivity of Graphite and Carbon at Low
#     Temperatures,
#     Robert A. Buerschaper.
# [7]
# http://chemistry.stackexchange.com/questions/820/electrical-conductivity-of-graphite
# [8] http://www.engineeringtoolbox.com/specific-heat-solids-d_154.html
# [9] http://www.azom.com/article.aspx?ArticleID=1630
# [10] A fine-grained, isotropic graphite for use as NBS thermophysical
#      property RM's from 5 to 2500 K;
#      Jerome G. Hust;
#      <http://www.nist.gov/srm/upload/SP260-89.PDF>.
# [12]
# http://www.engineeringtoolbox.com/linear-expansion-coefficients-d_95.html
# [14] http://aries.ucsd.edu/LIB/PROPS/PANOS/c.html
#
# Carbon doesn't actually melt at atmospheric pressure,
# but sublimes.
melting_point = 3900.0
magnetic_permeability = 0.999984 * mu0


def electrical_conductivity(T):
    '''Data from :cite:`KP:2003:TNI`.
    '''
    return 1e6 / (28.9 - 18.8 * numpy.exp(-(numpy.log(T/1023.0)/2.37)**2))


def density(T):
    ''':cite:`Morgan72` gives the thermal expansion coefficients parallel
    and perpendicular to the basal plane.
    '''
    # TODO better temperature dependence
    return 2.267e3 / (1 + 30.0e-6*(T-298.0))


def specific_heat_capacity(T):
    '''Data from :cite:`BM73`.
    '''
    return 4.184e3 * (
        + 0.538657
        + 9.11129e-6 * T
        - 90.2725 / T
        - 43449.3 / T**2
        + 1.59309e7 / T**3
        - 1.43688e9 / T**4
        )


def thermal_conductivity(T):
    # Data from [9] (except for the outlier at T=2000K),
    # perpendicular to the layers.
    # Quadratic least-squares fit of 1/c_p.
    return 1.0 / (-9.797e-08*T**2 + 0.0007809*T - 0.05741)
