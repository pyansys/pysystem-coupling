#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.settings.datamodel import *

from .attribute_child import attribute_child


class attribute(NamedObject[attribute_child]):
    """
    Set the variable's attributes.
    """

    syc_name = "Attribute"

    child_object_type: attribute_child = attribute_child
    """
    child_object_type of attribute.
    """
