import numpy as np
from scipy.optimize import root_scalar
from pyroll.core import BaseRollPass, Hook

VERSION = "3.0.0"


@BaseRollPass.extension_class
class InterfaceFriction(BaseRollPass):
    coulomb_friction_coefficient = Hook[float]()
    """Friction coefficient for sliding friction resulting from Coulombs friction model."""

    friction_factor = Hook[float]()
    """Friction factor for sticking friction."""


@BaseRollPass.coulomb_friction_coefficient
def coulomb_friction_coefficient(self: InterfaceFriction):
    if self.has_set_or_cached("friction_factor"):
        return self.friction_factor / (
                1 + np.pi / 2 + np.arccos(self.friction_factor) + np.sqrt(1 - self.friction_factor ** 2))
    else:
        raise ValueError(
            "Please provide either Coulomb's friction coefficient or a friction factor to use the pyroll-interface-friction-plugin.")


@BaseRollPass.friction_factor
def friction_factor(self: InterfaceFriction):
    if self.has_set("coulomb_friction_coefficient"):

        def eq(m: float):
            return self.coulomb_friction_coefficient - (m / (1 + np.pi / 2 + np.arccos(m) + np.sqrt(1 - m ** 2)))

        sol = root_scalar(eq, bracket=[0, 1])
        
        return sol.root
    else:
        raise ValueError(
            "Please provide either Coulomb's friction coefficient or a friction factor to use the pyroll-interface-friction-plugin.")
