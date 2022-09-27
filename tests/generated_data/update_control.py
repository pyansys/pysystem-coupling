#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.impl.types import *


class update_control(Container):
    """
    'update_control' child.
    """

    syc_name = "UpdateControl"

    property_names_types = [
        ("option", "Option", "str"),
        ("update_frequency", "UpdateFrequency", "int"),
    ]

    @property
    def option(self) -> str:
        """'option' property of 'child_object_type' object"""
        return self.get_property_state("option")

    @option.setter
    def option(self, value: str):
        self.set_property_state("option", value)

    @property
    def update_frequency(self) -> int:
        """'update_frequency' property of 'child_object_type' object"""
        return self.get_property_state("update_frequency")

    @update_frequency.setter
    def update_frequency(self, value: int):
        self.set_property_state("update_frequency", value)
