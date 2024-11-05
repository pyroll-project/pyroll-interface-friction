from typing import Union

import numpy as np
from pyroll.core import ThreeRollPass, Roll, CircularOvalGroove
from pyroll.interface_friction import InterfaceFriction


def test_friction_coefficient():
    rp: Union[InterfaceFriction, ThreeRollPass] = ThreeRollPass(label="Oval I",
                                                                roll=Roll(
                                                                    groove=CircularOvalGroove(
                                                                        depth=8e-3,
                                                                        r1=6e-3,
                                                                        r2=40e-3
                                                                    ),
                                                                    nominal_radius=160e-3,
                                                                    rotational_frequency=1,
                                                                ),
                                                                gap=2e-3
                                                                )

    rp.friction_factor = 0.8

    assert np.allclose(rp.coulomb_friction_coefficient, 0.209, rtol=1e-2)


def test_friction_factor():
    rp: Union[InterfaceFriction, ThreeRollPass] = ThreeRollPass(label="Oval I",
                                                                roll=Roll(
                                                                    groove=CircularOvalGroove(
                                                                        depth=8e-3,
                                                                        r1=6e-3,
                                                                        r2=40e-3
                                                                    ),
                                                                    nominal_radius=160e-3,
                                                                    rotational_frequency=1,
                                                                ),
                                                                gap=2e-3,
                                                                )
    rp.coulomb_friction_coefficient = 0.209

    assert np.allclose(rp.friction_factor, 0.8, rtol=1e-2)
