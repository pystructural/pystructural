from pystructural.core import Element
from pystructural.core import DOF

__all__ = ['LinearTriangleElement2D']


class LinearTriangleElement2D(Element):
    def __init__(self):
        super().__init__()

    def get_dof(self):
        return DOF(displacement_x=True, displacement_y=True)

    def shape_function(self, i):
        pass

    def compute_shape_matrix(self):
        pass

    def compute_strain_matrix(self):
        pass

    def compute_stiffness_matrix(self):
        pass

    def compute_mass_matrix(self):
        pass

    def compute_nodal_force_vector(self):
        pass