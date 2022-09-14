#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.datamodel import *


class unmapped_value_options(Group):
    """
    'unmapped_value_options' child.
    """

    syc_name = "UnmappedValueOptions"

    property_names_types = [
        ("matrix_verbosity", "MatrixVerbosity", "Integer"),
        ("solver_verbosity", "SolverVerbosity", "Integer"),
        ("solver", "Solver", "String"),
        ("solver_relative_tolerance", "SolverRelativeTolerance", "Real"),
        ("solver_max_iterations", "SolverMaxIterations", "Integer"),
        ("solver_max_search_directions", "SolverMaxSearchDirections", "Integer"),
        ("preconditioner", "Preconditioner", "String"),
        ("ilut_tau", "IlutTau", "Real"),
        ("ilut_max_fill", "IlutMaxFill", "Integer"),
        ("ilut_pivot_tol", "IlutPivotTol", "Real"),
        ("face_filter_tolerance", "FaceFilterTolerance", "Real"),
        ("rbf_shape_parameter", "RbfShapeParameter", "Real"),
        ("rbf_linear_correction", "RbfLinearCorrection", "Boolean"),
        ("rbf_colinearity_tolerance", "RbfColinearityTolerance", "Real"),
    ]

    @property
    def matrix_verbosity(self) -> Integer:
        """'matrix_verbosity' property of 'analysis_control' object"""
        return self.get_property_state("matrix_verbosity")

    @matrix_verbosity.setter
    def matrix_verbosity(self, value: Integer):
        self.set_property_state("matrix_verbosity", value)

    @property
    def solver_verbosity(self) -> Integer:
        """'solver_verbosity' property of 'analysis_control' object"""
        return self.get_property_state("solver_verbosity")

    @solver_verbosity.setter
    def solver_verbosity(self, value: Integer):
        self.set_property_state("solver_verbosity", value)

    @property
    def solver(self) -> String:
        """'solver' property of 'analysis_control' object"""
        return self.get_property_state("solver")

    @solver.setter
    def solver(self, value: String):
        self.set_property_state("solver", value)

    @property
    def solver_relative_tolerance(self) -> Real:
        """'solver_relative_tolerance' property of 'analysis_control' object"""
        return self.get_property_state("solver_relative_tolerance")

    @solver_relative_tolerance.setter
    def solver_relative_tolerance(self, value: Real):
        self.set_property_state("solver_relative_tolerance", value)

    @property
    def solver_max_iterations(self) -> Integer:
        """'solver_max_iterations' property of 'analysis_control' object"""
        return self.get_property_state("solver_max_iterations")

    @solver_max_iterations.setter
    def solver_max_iterations(self, value: Integer):
        self.set_property_state("solver_max_iterations", value)

    @property
    def solver_max_search_directions(self) -> Integer:
        """'solver_max_search_directions' property of 'analysis_control' object"""
        return self.get_property_state("solver_max_search_directions")

    @solver_max_search_directions.setter
    def solver_max_search_directions(self, value: Integer):
        self.set_property_state("solver_max_search_directions", value)

    @property
    def preconditioner(self) -> String:
        """'preconditioner' property of 'analysis_control' object"""
        return self.get_property_state("preconditioner")

    @preconditioner.setter
    def preconditioner(self, value: String):
        self.set_property_state("preconditioner", value)

    @property
    def ilut_tau(self) -> Real:
        """'ilut_tau' property of 'analysis_control' object"""
        return self.get_property_state("ilut_tau")

    @ilut_tau.setter
    def ilut_tau(self, value: Real):
        self.set_property_state("ilut_tau", value)

    @property
    def ilut_max_fill(self) -> Integer:
        """'ilut_max_fill' property of 'analysis_control' object"""
        return self.get_property_state("ilut_max_fill")

    @ilut_max_fill.setter
    def ilut_max_fill(self, value: Integer):
        self.set_property_state("ilut_max_fill", value)

    @property
    def ilut_pivot_tol(self) -> Real:
        """'ilut_pivot_tol' property of 'analysis_control' object"""
        return self.get_property_state("ilut_pivot_tol")

    @ilut_pivot_tol.setter
    def ilut_pivot_tol(self, value: Real):
        self.set_property_state("ilut_pivot_tol", value)

    @property
    def face_filter_tolerance(self) -> Real:
        """'face_filter_tolerance' property of 'analysis_control' object"""
        return self.get_property_state("face_filter_tolerance")

    @face_filter_tolerance.setter
    def face_filter_tolerance(self, value: Real):
        self.set_property_state("face_filter_tolerance", value)

    @property
    def rbf_shape_parameter(self) -> Real:
        """'rbf_shape_parameter' property of 'analysis_control' object"""
        return self.get_property_state("rbf_shape_parameter")

    @rbf_shape_parameter.setter
    def rbf_shape_parameter(self, value: Real):
        self.set_property_state("rbf_shape_parameter", value)

    @property
    def rbf_linear_correction(self) -> Boolean:
        """'rbf_linear_correction' property of 'analysis_control' object"""
        return self.get_property_state("rbf_linear_correction")

    @rbf_linear_correction.setter
    def rbf_linear_correction(self, value: Boolean):
        self.set_property_state("rbf_linear_correction", value)

    @property
    def rbf_colinearity_tolerance(self) -> Real:
        """'rbf_colinearity_tolerance' property of 'analysis_control' object"""
        return self.get_property_state("rbf_colinearity_tolerance")

    @rbf_colinearity_tolerance.setter
    def rbf_colinearity_tolerance(self, value: Real):
        self.set_property_state("rbf_colinearity_tolerance", value)
