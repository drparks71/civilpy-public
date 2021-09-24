import civilpy

unit = civilpy.unit

# Establish constants
gravity = 32.2 * (unit.ft / (unit.second ** 2))
gravity_m = 9.81 * (unit.meter / (unit.second ** 2))
gravity_c = 32.2 * (unit.lb * unit.ft / unit.lbf * unit.sec ** 2)


def kinetic_energy(m, v, system='english'):
    if str.lower(system) == 'english':
        value = (m * (v ** 2)) / (2 * gravity)
    elif str.lower(system) == 'metric':
        value = (m * (v ** 2)) / (2 * gravity_m)
    else:
        print('Error: only metric or english may be used as system variable strings')

    return value


def potential_energy(m, z, system='english'):
    if str.lower(system) == 'english':
        value = (m * z * gravity)
    elif str.lower(system) == 'metric':
        value = (m * z * gravity_m)
    else:
        print('Error: only metric or english may be used as system variable strings')

    return value


def mass_to_weight(m, system='english'):
    if str.lower(system) == 'english':
        value = (m * gravity)
    elif str.lower(system) == 'metric':
        value = (m * gravity_m)
    else:
        print('Error: only metric or english may be used as system variable strings')

    return value

def specific_weight(density):
    gamma = civilpy.general.physics.gravity * density
    return gamma

class density:
    air_stp = 0.0807 * unit.lbf / unit.ft ** 3
    air = 0.075 * unit.lbf / unit.ft ** 3
    alcohol = 49.3 * unit.lbf / unit.ft ** 3
    ammonia = 38 * unit.lbf / unit.ft ** 3
    gasoline = 44.9 * unit.lbf / unit.ft ** 3
    glycerin = 78.8 * unit.lbf / unit.ft ** 3
    mercury = 848 * unit.lbf / unit.ft ** 3
    water = 62.4 * unit.lbf / unit.ft ** 3



