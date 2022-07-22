#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.settings.datamodel import *


class update_control(Group):
    """
    Available for AEDT participants running an Eddy Current solution when the coupled analysis is steady.
    """

    syc_name = "UpdateControl"

    property_names_types = [
        ("option", "Option", "String"),
        ("update_frequency", "UpdateFrequency", "Integer"),
    ]

    @property
    def option(self) -> String:
        """Specifies how often the participant will perform updates."""
        return self.get_property_state("option")

    @option.setter
    def option(self, value: String):
        self.set_property_state("option", value)

    @property
    def update_frequency(self) -> Integer:
        """Available when the UpdateControl.Option is set to StepInterval."""
        return self.get_property_state("update_frequency")

    @update_frequency.setter
    def update_frequency(self, value: Integer):
        self.set_property_state("update_frequency", value)
