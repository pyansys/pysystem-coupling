#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.impl.datamodel import *

from .variable_child import variable_child


class variable(NamedObject[variable_child]):
    """
    Configure a variable for the coupling participant.
    """

    syc_name = "Variable"

    child_object_type: variable_child = variable_child
    """
    child_object_type of variable.
    """
