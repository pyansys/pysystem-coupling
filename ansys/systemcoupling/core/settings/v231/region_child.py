#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.settings.datamodel import *


class region_child(Group):
    """
    Define the region's settings.
    """

    syc_name = "child_object_type"

    property_names_types = [
        ("topology", "Topology", "String"),
        ("input_variables", "InputVariables", "StringList"),
        ("output_variables", "OutputVariables", "StringList"),
        ("display_name", "DisplayName", "String"),
        ("region_discretization_type", "RegionDiscretizationType", "String"),
    ]

    @property
    def topology(self) -> String:
        """Type of data being transferred from/to the region."""
        return self.get_property_state("topology")

    @topology.setter
    def topology(self, value: String):
        self.set_property_state("topology", value)

    @property
    def input_variables(self) -> StringList:
        """Variables for which the region can receive data."""
        return self.get_property_state("input_variables")

    @input_variables.setter
    def input_variables(self, value: StringList):
        self.set_property_state("input_variables", value)

    @property
    def output_variables(self) -> StringList:
        """Variables for which the region can send data."""
        return self.get_property_state("output_variables")

    @output_variables.setter
    def output_variables(self, value: StringList):
        self.set_property_state("output_variables", value)

    @property
    def display_name(self) -> String:
        """Region name to be displayed in user-facing communications."""
        return self.get_property_state("display_name")

    @display_name.setter
    def display_name(self, value: String):
        self.set_property_state("display_name", value)

    @property
    def region_discretization_type(self) -> String:
        """**CURRENTLY NOT DOCUMENTED**"""
        return self.get_property_state("region_discretization_type")

    @region_discretization_type.setter
    def region_discretization_type(self, value: String):
        self.set_property_state("region_discretization_type", value)
