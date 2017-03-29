import materials


def test_water():
    materials.water.density(0.0)
    materials.water.dynamic_viscosity(0.0)
    materials.water.specific_heat_capacity(0.0)
    materials.water.thermal_conductivity(0.0)
    return
