#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.adaptor.impl.datamodel import *

from .expression_function_child import expression_function_child


class expression_function(NamedObject[expression_function_child]):
    """
    Makes an external Python function accessible from expressions.
    """

    syc_name = "ExpressionFunction"

    child_object_type: expression_function_child = expression_function_child
    """
    child_object_type of expression_function.
    """
