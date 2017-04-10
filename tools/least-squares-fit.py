#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Compute least-squares fit for a given data set.
'''
import numpy as np


def _density_water():
    # Data from
    # https://en.wikipedia.org/wiki/Properties_of_water#Density_of_water_and_ice
    x = [0, 4, 10, 15, 20, 22, 25, 30, 40, 60, 80, 100]
    y = [999.8395, 999.9720, 999.7026, 999.1026, 998.2071, 997.7735, 997.0479,
         995.6502, 992.2, 983.2, 971.8, 958.4]
    return x, y


def _spec_heat_water():
    '''
    Specific heat data of water.
    '''
    # Data source:
    # http://www.tainstruments.co.jp/application/pdf/Thermal_Library/Applications_Notes/TN015.PDF
    x = np.array(range(0, 101)) + 273.15
    y = [4.2177, 4.2141, 4.2107, 4.2077, 4.2048, 4.2022, 4.1999, 4.1977,
         4.1957, 4.1939, 4.1922, 4.1907, 4.1893, 4.1880, 4.1869, 4.1858,
         4.1849, 4.1840, 4.1832, 4.1825, 4.1819, 4.1813, 4.1808, 4.1804,
         4.1800, 4.1796, 4.1793, 4.1790, 4.1788, 4.1786, 4.1785, 4.1784,
         4.1783, 4.1783, 4.1782, 4.1782, 4.1783, 4.1783, 4.1784, 4.1785,
         4.1786, 4.1787, 4.1789, 4.1791, 4.1792, 4.1795, 4.1797, 4.1799,
         4.1802, 4.1804, 4.1807, 4.1810, 4.1814, 4.1817, 4.1820, 4.1824,
         4.1828, 4.1832, 4.1836, 4.1840, 4.1844, 4.1849, 4.1853, 4.1858,
         4.1863, 4.1868, 4.1874, 4.1879, 4.1885, 4.1890, 4.1896, 4.1902,
         4.1908, 4.1915, 4.1921, 4.1928, 4.1935, 4.1942, 4.1949, 4.1957,
         4.1964, 4.1972, 4.1980, 4.1988, 4.1997, 4.2005, 4.2014, 4.2023,
         4.2032, 4.2042, 4.2051, 4.2061, 4.2071, 4.2081, 4.2092, 4.2103,
         4.2114, 4.2125, 4.2136, 4.2148, 4.2160]
    y = np.array(y) * 1.0e3
    return x, y


def _therm_cond_graphite():
    # thermal conductivity of graphite from
    # http://aries.ucsd.edu/LIB/PROPS/PANOS/c.html
    x = [300, 400, 500, 600, 645, 800, 1000, 1200, 1500,
         2500, 3000]
    y = [5.7, 4.09, 3.49, 2.68, 2.45, 2.01, 1.60, 1.34, 1.08,
         0.81, 0.70]
    y = 1 / np.array(y)
    # from matplotlib import pyplot as pp
    # pp.plot(x, 1/np.array(y), 'o')
    # pp.show()
    return x, y


def _spec_heat_sic():
    # specific heat of SiC,
    # <http://www.ceramics.nist.gov/srd/summary/scdscs.htm>.
    x = [20, 500, 1000, 1200, 1400, 1500]
    x = np.array(x) + 273.15
    y = [715, 1086, 1240, 1282, 1318, 1336]
    return x, y


def _vol_exp_sic():
    # volume expansion coefficient of SiC
    x = [500, 600, 900, 1500, 2100]
    y = [3.8e-6, 4.3e-6, 4.8e-6, 5.5e-6, 5.5e-6]
    return x, y


def _elec_res_copper():
    # electrical resistivity of copper:
    # http://www.nist.gov/data/PDFfiles/jpcrd155.pdf
    x = [273.15, 293, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1100,
         1200, 1300, 1357.6]
    y = [1.543, 1.678, 1.725, 2.063, 2.402, 3.090, 3.792, 4.514, 5.262, 6.041,
         6.858, 7.717, 8.626, 9.592, 10.171]
    return x, y


def _density_mercury():
    # Herington, E. F. G., Brown, I., Lane, J. E., Ambrose, D.,
    # Pure Appz.. Chem. 1976, 45, 1-9.
    # https://srdata.nist.gov/soliubility/IUPAC/SDS-29/SDS-29-pages_237.pdf
    x = [
        253.15, 258.15, 263.15, 268.15, 273.15, 278.15, 283.15, 288.15, 293.15,
        298.15, 303.15, 308.15, 313.15, 318.15, 323.15, 328.15, 333.15, 343.15,
        348.15, 353.15, 358.15, 363.15, 368.15, 373.15, 383.15, 393.15, 403.15,
        413.15, 423.15, 433.15, 443.15, 453.15, 463.15, 473.15, 483.15, 493.15,
        503.15, 513.15, 523.15, 533.15, 543.15, 553.15, 563.15, 573.15,
        ]
    y = [
        13.64459, 13.63218, 13.61978, 13.60743, 13.59508, 13.58276, 13.57044,
        13.55815, 13.54587, 13.53362, 13.52137, 13.50914, 13.49693, 13.48473,
        13.47253, 13.46038, 13.44823, 13.42397, 13.41186, 13.39977, 13.38767,
        13.37560, 13.36354, 13.3515, 13.3274, 13.3034, 13.2794, 13.2554,
        13.2315, 13.2076, 13.1837, 13.1598, 13.1360, 13.1121, 13.0883, 13.0645,
        13.0407, 13.0169, 12.9930, 12.9692, 12.9454, 12.9215, 12.8976, 12.8737,
        ]

    return x, y


def _main(x, y, degree):
    # form the Vandermonde matrix
    A = np.vander(x, degree+1)

    # find the x that minimizes the norm of Ax-y
    (coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, y)

    print('Singular values of the Vandermonde matrix:')
    print(sing_vals)
    print
    print('Rank: %d' % rank)
    print
    if rank < degree+1:
        raise RuntimeError('Ill-conditioned problem. Byes.')

    # create a polynomial using coefficients
    f = np.poly1d(coeffs)
    print(f)

    # f(x) == np.dot(A,coeffs)
    res = (f(x) - y)
    print
    print('||r||_1   = %e' % np.linalg.norm(res, 1))
    print('||r||_2   = %e' % np.linalg.norm(res, 2))
    print('||r||_inf = %e' % np.linalg.norm(res, np.inf))

    from matplotlib import pyplot as pp

    # least-squares polynomial
    X = np.linspace(min(x), max(x), 100)
    pp.plot(X, f(X), '-')

    # data points
    pp.plot(x, y, 'o')

    pp.show()
    return


if __name__ == '__main__':
    x, y = _density_mercury()
    _main(x, y, degree=2)
