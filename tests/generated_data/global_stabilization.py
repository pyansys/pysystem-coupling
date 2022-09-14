#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.datamodel import *


class global_stabilization(Group):
    """
    'global_stabilization' child.
    """

    syc_name = "GlobalStabilization"

    property_names_types = [
        ("option", "Option", "String"),
        ("initial_iterations", "InitialIterations", "Integer"),
        ("initial_relaxation_factor", "InitialRelaxationFactor", "Real"),
        ("maximum_retained_time_steps", "MaximumRetainedTimeSteps", "Integer"),
        ("maximum_retained_iterations", "MaximumRetainedIterations", "Integer"),
        ("diagnostics_level", "DiagnosticsLevel", "Integer"),
        ("weight_option", "WeightOption", "String"),
        ("qr_tol_this_step", "QRTolThisStep", "Real"),
        ("qr_tol_old_steps", "QRTolOldSteps", "Real"),
    ]

    @property
    def option(self) -> String:
        """'option' property of 'analysis_control' object"""
        return self.get_property_state("option")

    @option.setter
    def option(self, value: String):
        self.set_property_state("option", value)

    @property
    def initial_iterations(self) -> Integer:
        """'initial_iterations' property of 'analysis_control' object"""
        return self.get_property_state("initial_iterations")

    @initial_iterations.setter
    def initial_iterations(self, value: Integer):
        self.set_property_state("initial_iterations", value)

    @property
    def initial_relaxation_factor(self) -> Real:
        """'initial_relaxation_factor' property of 'analysis_control' object"""
        return self.get_property_state("initial_relaxation_factor")

    @initial_relaxation_factor.setter
    def initial_relaxation_factor(self, value: Real):
        self.set_property_state("initial_relaxation_factor", value)

    @property
    def maximum_retained_time_steps(self) -> Integer:
        """'maximum_retained_time_steps' property of 'analysis_control' object"""
        return self.get_property_state("maximum_retained_time_steps")

    @maximum_retained_time_steps.setter
    def maximum_retained_time_steps(self, value: Integer):
        self.set_property_state("maximum_retained_time_steps", value)

    @property
    def maximum_retained_iterations(self) -> Integer:
        """'maximum_retained_iterations' property of 'analysis_control' object"""
        return self.get_property_state("maximum_retained_iterations")

    @maximum_retained_iterations.setter
    def maximum_retained_iterations(self, value: Integer):
        self.set_property_state("maximum_retained_iterations", value)

    @property
    def diagnostics_level(self) -> Integer:
        """'diagnostics_level' property of 'analysis_control' object"""
        return self.get_property_state("diagnostics_level")

    @diagnostics_level.setter
    def diagnostics_level(self, value: Integer):
        self.set_property_state("diagnostics_level", value)

    @property
    def weight_option(self) -> String:
        """'weight_option' property of 'analysis_control' object"""
        return self.get_property_state("weight_option")

    @weight_option.setter
    def weight_option(self, value: String):
        self.set_property_state("weight_option", value)

    @property
    def qr_tol_this_step(self) -> Real:
        """'qr_tol_this_step' property of 'analysis_control' object"""
        return self.get_property_state("qr_tol_this_step")

    @qr_tol_this_step.setter
    def qr_tol_this_step(self, value: Real):
        self.set_property_state("qr_tol_this_step", value)

    @property
    def qr_tol_old_steps(self) -> Real:
        """'qr_tol_old_steps' property of 'analysis_control' object"""
        return self.get_property_state("qr_tol_old_steps")

    @qr_tol_old_steps.setter
    def qr_tol_old_steps(self, value: Real):
        self.set_property_state("qr_tol_old_steps", value)
