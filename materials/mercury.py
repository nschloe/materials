# -*- coding: utf-8 -*-
#
# [1] Herington, E. F. G., Brown, I., Lane, J. E., Ambrose, D.,
#     Pure Appz.. Chem. 1976, 45, 1-9.
#     https://srdata.nist.gov/soliubility/IUPAC/SDS-29/SDS-29-pages_237.pdf


def density(T):
    '''Least-squares fit from [1].
    '''
    return 1.542e-07 * T**2 - 0.002531 * T + 14.27
