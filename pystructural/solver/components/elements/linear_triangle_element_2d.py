from pystructural.solver.components import DOF
from pystructural.solver.components.elements import Element

from pystructural.solver.components.geometries import *

__all__ = ['LinearTriangleElement2D']


class LinearTriangleElement2D(Element):
    compatible_geometry = Triangle2D
    compatible_materials = []
    compatible_element_geometries = []
    element_dimension = 6

    def __init__(self):
        super().__init__()

    def get_dof(self):
        return DOF(displacement_x=True, displacement_y=True)

    def get_stiffness_coordinate_to_node_and_dof_variable(self, x):
        pass

    def get_node_and_dof_variable_to_stiffness_coordinate(self, node_id, dof_id):
        pass

    def compute_element_properties(self):
        pass

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
