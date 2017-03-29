import materials
import matplotlib.pyplot as plt
import numpy


T = numpy.linspace(274.0, 370.0, num=100)

rho_air = materials.air.density(T)
rho_argon = materials.argon.density(T)
rho_copper = materials.copper.density(T)
rho_water = materials.water.density(T)

plt.semilogy(T, rho_copper, label='copper')
plt.semilogy(T, rho_water, label='water')
plt.semilogy(T, rho_argon, label='argon')
plt.semilogy(T, rho_air, label='air')

plt.title('densities')
plt.xlabel('temperature (K)')
plt.ylabel('density (kg/m^3)')
plt.legend()

plt.show()
