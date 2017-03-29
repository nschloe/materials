import materials


def test_air():
    materials.air.density(273.0)
    materials.air.specific_heat_capacity(273.0)
    materials.air.thermal_conductivity(273.0)
    return


def test_argon():
    materials.argon.density(273.0)
    return


def test_copper():
    materials.copper.density(273.0)
    materials.copper.electrical_conductivity(273.0)
    materials.copper.specific_heat_capacity(273.0)
    materials.copper.thermal_conductivity(273.0)
    return


def test_gallium_arsenide_liquid():
    materials.gallium_arsenide_liquid.density(273.0)
    materials.gallium_arsenide_liquid.dynamic_viscosity(273.0)
    return


def test_gallium_arsenide_solid():
    materials.gallium_arsenide_solid.density(273.0)
    materials.gallium_arsenide_solid.specific_heat_capacity(273.0)
    materials.gallium_arsenide_solid.thermal_conductivity(273.0)
    return


def test_graphite():
    materials.graphite.density(273.0)
    materials.graphite.electrical_conductivity(273.0)
    materials.graphite.specific_heat_capacity(273.0)
    materials.graphite.thermal_conductivity(273.0)
    return


def test_silicon_carbide():
    materials.silicon_carbide.density(273.0)
    materials.silicon_carbide.thermal_conductivity(273.0)
    materials.silicon_carbide.thermal_diffusivity(273.0)
    return


def test_water():
    materials.water.density(273.0)
    materials.water.dynamic_viscosity(273.0)
    materials.water.specific_heat_capacity(273.0)
    materials.water.thermal_conductivity(273.0)
    return
