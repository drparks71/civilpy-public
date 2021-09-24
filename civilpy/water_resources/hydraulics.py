import civilpy.general
import numpy as np


def hydraulic_radius(depth, dia=0, b1=0, b2=0, h=0, slope=0, shape='circle'):
    if shape == 'circle':
        theta = 2 * np.arccos(((dia/2) - depth) / (dia / 2))
        p = (dia / 2) * theta
        a = ((dia / 2) ** 2) * ((theta - np.sin(theta)) / 2)
        radius = a / p

    elif shape == 'rectangle':
        p = b1 + depth + depth
        a = depth * b1
        radius = a / p

    elif shape == 'trapezoid':
        if slope == 0:
            slope = abs(b1 - b2) / h
            b_water = b1 + 2 * depth * slope
            a = (depth * (b1 + b_water)) / 2
            p = b1 + 2 * depth * np.sqrt(1 + (slope ** 2))
        elif slope != 0:
            b_water = b1 + 2 * depth * slope
            a = (depth * (b1 + b_water)) / 2
            p = b1 + 2 * depth * np.sqrt(1 + (slope ** 2))
        radius = a / p

    elif shape == 'triangle':
        a = (depth ** 2) * slope
        p = 2 * np.sqrt((depth ** 2 * (1 + slope ** 2)))
        radius = a / p

    return radius

def specific_gravity(density, phase='liquid'):
    if phase == 'liquid':
        sg = density / civilpy.general.density.water
        return sg
    elif phase == 'gas':
        sg = density / civilpy.general.density.air_stp
        return sg
    else:
        print('phase must be liquid or gas, for gas assumes pressure = 1 atm and temp = 70F')

def manometer_pressure(rho_medium, h, rho1=0, h1=0, rho2=0, h2=0):
    g = civilpy.general.physics.gravity
    g_c = civilpy.general.physics.gravity_c
    delta = (g / g) * (rho_medium * h + rho1 * h1 - rho2 * h2)

    return delta

def pressure_at_depth(height, rho=0):
    if rho == 0:
        rho = 62.4 * civilpy.unit.lb / civilpy.unit.ft ** 3

    p = rho * civilpy.general.physics.gravity * height

    return p

